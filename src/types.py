from enum import Enum
from typing import Union, Optional

# CFG :
#   Expr -> Term Expr' | PreOperator Term Expr' |
#   Expr' -> Operator Expr Expr' | ε
#   Term -> Factor PosOperator 
#   Factor -> Var | Number | '(' Expr ')' | FuncDefinition | Piecewise
#   Piecewise -> Bounds | Bounds ',' Piecewise
#   Bounds -> Expr 'For' Expr
#   FuncDefinition -> Var PosOperator '(' ExprList ')' = Expr | 
#                     Var PosOperator '(' ExprList ')' Expr'
#   ExprList -> Expr | Expr ',' ExprList
#   Operator -> = | ≈ | + | - | * | / | ** | < | > | ≪ | ≫ | <= | >= | ... 
#   PreOperator -> - | √ | ! | ∫ | ∑ | ∏ | ∮ | ∇ | ∂ | d | ∆ | | (abs) |
#   PosOperator -> ! | ' | ° | · | : | % | ... | | (abs) |
#   Var -> ([a-zA-z_][a-zA-Z0-9_]*) | ∞ | λ | μ | ρ | σ | τ | θ | Θ | Φ | Ψ | Ω | ω | Γ | γ | β 
#   Number -> Integer | Float | e | π | i

# Lexer Stuff #
tokens = [
    ('NUMBER',      r'\b\d+(\.\d*)?|e|π|i\b'),         # Integer, Float, e, π, i
    ('OPERATOR',    r'[=≈+\-*/]|(\*\*)|[<>]|(≪)|(≫)|[<=]|[>=]|...'), # Various operators
    ('PREOPERATOR', r'[√!∫∑∏∮∇∂d∆\|]'),                # PreOperators
    ('POSOPERATOR', r'[!\'°·:%\|]'),                   # PostOperators
    ('LPAREN',      r'\('),                            # Left Parenthesis
    ('RPAREN',      r'\)'),                            # Right Parenthesis
    ('COMMA',       r','),                             # Comma
    ('FOR',         r'\bFor\b'),                       # 'For' keyword
    ('VAR',         r'\b[a-zA-z_][a-zA-Z0-9_]*|[∞λμρστθΘΦΨΩωΓγβ]\b'),  # Variables and Greek letters
    ('SKIP',        r'[ \t]+'),                        # Spaces and tabs                   
    ('MISMATCH',    r'.'),                             # Any other character
]

# Parser Stuff #
# A number n
class Number:
    def __init__(self, value):
        self.value = value

# A variable x
class Var:
    def __init__(self, name: str):
        self.name = name

# A Operator is a +, -, *, /, **, <, >, <=, >=, =, ≈, ...
class Operator:
    def __init__(self, operator: str):
        self.operator = operator

# A PreOperator is a -, √, !, ∫, ∑, ∏, ∮, ∇, ∂, d, ∆, |
class PreOperator:
    def __init__(self, operator: str):
        self.operator = operator

# A PosOperator is a !, ', °, ·, :, %, ..., |
class PosOperator:
    def __init__(self, operator: str):
        self.operator = operator

# An Expr is a Term and an Expr' or a PreOperator, a Term, and an Expr'
class Expr:
    def __init__(self, preOperator: Optional['PreOperator'], term: 'Term', exprPrime: Optional['ExprPrime']):
        self.preOperator = preOperator
        self.term = term
        self.exprPrime = exprPrime

# An Expr' is an Operator, an Expr, and an Expr' or nothing
class ExprPrime:
    def __init__(self, operator: Optional['Operator'], expr: Optional['Expr'], exprPrime: Optional['ExprPrime']):
        self.operator = operator
        self.expr = expr
        self.exprPrime = exprPrime

# A Term is a Factor and a PosOperator
class Term:
    def __init__(self, factor: 'Factor', posOperator: Optional['PosOperator']):
        self.factor = factor
        self.posOperator = posOperator

# A Factor is a Var, a Number, a FuncDefinition, a Piecewise, or an Expr bounded by parentheses
class Factor:
    def __init__(self, factor: Union['Var', 'Number', 'FuncDefinition', 'Piecewise', 'Expr']):
        self.factor = factor

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

# A FuncDefinition is a Var, a PosOperator, an ExprList in parens, and an Expr or an ExprPrime
class FuncDefinition:
    def __init__(self, var: 'Var', posOperator: Optional['PosOperator'], exprList: 'ExprList', expr: Optional['Expr'], exprPrime: Optional['ExprPrime']):
        self.var = var
        self.posOperator = posOperator
        self.exprList = exprList
        self.expr = expr
        self.exprPrime = exprPrime

# An ExprList is a list of Exprs
class ExprList:
    def __init__(self, expr: 'Expr', exprList: Optional['ExprList']):
        self.expr = expr
        self.exprList = exprList