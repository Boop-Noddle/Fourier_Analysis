from enum import Enum
from typing import Union

# CFG :
#   Expr -> Term | Expr Operator Expr | '(' Expr ')' 
#   Term -> Var | Number | '(' Expr ')' | FuncDefinition | Piecewise
#   Piecewise -> Bounds | Bounds ',' Piecewise
#   Bounds -> Expr 'For' Expr
#   FuncDefinition -> FuncName '(' ExprLIst ')'
#   FuncName -> ([a-zA-Z_][a-zA-Z0-9_]*)
#   ExprList -> Expr | Expr ',' ExprList
#   Operator -> = | + | - | * | / | ** | < | > | <= | >= | √ | !
#   Var -> ([a-zA-z_][a-zA-Z0-9]*) | ([a-zA-Z_][a-zA-Z_0-9]*) | ∞ | -∞ 
#   Number -> Integer | Float | -?e | -?pi | -?i 

# Lexer Stuff #
class ExprToken(Enum):
    RParen = 1
    LParen = 2
    Var = 3
    Plus = 4
    Sub = 5
    Mul = 6
    Div = 7
    Power = 8
    Equals = 9
    LessThen = 10
    GreaterThen = 11
    LessThenEqual = 12
    GreaterThenEqual = 13
    Sqrt = 14
    Factorial = 15
    Comma = 16
    Imaginary = 17
    Euler = 18
    Pi = 19
    EOF = 20

# Parser Stuff #
    
# A number n
class Number:
    def __init__(self, value):
        self.value = value

# A variable x
class Var:
    def __init__(self, name: str):
        self.name = name

# A Operator is a +, -, *, /, **, <, >, <=, >=, √, !
class Operator:
    def __init__(self, operator: str):
        self.operator = operator

# A Term can be a number, a variable, An Expr in parens, 
# or a function definition, or a piecewise
class Term:
    def __init__(self, number: 'Number', variable: 'Var', expr: 'Expr', func: 'FuncDefinition', piecewise: 'Piecewise'):
        self.number = number
        self.variable = variable
        self.expr = expr
        self.func = func
        self.piecewise = piecewise

# A Piecewise is a list of Bounds
class Piecewise:
    def __init__(self, bounds: 'Bounds', piecewise: 'Piecewise'):
        self.bounds = bounds
        self.piecewise = piecewise

# A Bounds is an Expr1 bounded by Expr2
class Bounds:
    def __init__(self, expr1: 'Expr', expr2: 'Expr'):
        self.expr1 = expr1
        self.expr2 = expr2

# A FuncDefinition is a function name and a list of Exprs
class FuncDefinition:
    def __init__(self, name: str, exprList: 'ExprList'):
        self.name = name
        self.exprList = exprList

# An ExprList is a list of Exprs
class ExprList:
    def __init__(self, expr: 'Expr', exprList: 'ExprList'):
        self.expr = expr
        self.exprList = exprList

# An Expr is a Term, or an Expr Operator Expr, or an Expr in parens
Expr = Union['Term', 'Operator', 'Expr']