from enum import Enum
from typing import Union, Optional

# CFG :
# Expr -> Term Expr' | '(' Expr ')' Expr'
# Expr' -> Operator Expr Expr' | ε
# Term -> Var | Number | '(' Expr ')' | FuncDefinition | Piecewise
# Piecewise -> Bounds | Bounds ',' Piecewise
# Bounds -> Expr 'For' Expr
# FuncDefinition -> FuncName '(' ExprList ')'
# FuncName -> ([a-zA-Z_][a-zA-Z0-9_]*)
# ExprList -> Expr | Expr ',' ExprList
# Operator -> = | + | - | * | / | ** | < | > | <= | >= | √ | !
# Var -> ([a-zA-z_][a-zA-Z0-9]*) | ([a-zA-Z_][a-zA-Z_0-9]*) | ∞ | -∞
# Number -> Integer | Float | -?e | -?pi | -?i


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

# An Expr' is an Operator, an Expr, and an Expr' or nothing
class ExprPrime:
    def __init__(self, operator: Optional[Operator], expr: Optional['Expr'], exprPrime: Optional['ExprPrime']):
        self.operator = operator
        self.expr = expr
        self.exprPrime = exprPrime

# A Term can be a number, a variable, An Expr in parens, 
# or a function definition, or a piecewise
class Term:
    def __init__(self, term: Union[Number, Var, 'Expr', 'FuncDefinition', 'Piecewise']):
        self.term = term

# A Piecewise is a list of Bounds
class Piecewise:
    def __init__(self, bounds: 'Bounds', piecewise: Optional['Piecewise']):
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
    def __init__(self, expr: 'Expr', exprList: Optional['ExprList']):
        self.expr = expr
        self.exprList = exprList

# Define Expr as Union of Term and ExprPrime
class Expr:
    def __init__(self, content: Union['Term', 'ExprPrime', 'Expr']):
        self.content = content