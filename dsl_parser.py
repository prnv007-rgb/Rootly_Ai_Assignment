from lark import Lark, Transformer
from ast_nodes import Series, Indicator, BinaryOp

grammar = """
?start: expr
?expr: expr "AND" term   -> and_op
     | term
?term: comparison
comparison: value OP value

?value: indicator
      | NAME
      | NUMBER

indicator: NAME "(" NAME "," NUMBER ")"

OP: ">" | "<" | ">=" | "<=" | "=="
NAME: /[a-zA-Z_]+/
NUMBER: /[0-9]+/

%import common.WS
%ignore WS
"""

class DSLTransformer(Transformer):
    def comparison(self, items):
        left, op, right = items

        if isinstance(left, str):
            left = Series(left)
        if isinstance(right, str):
            right = Series(right)

        return BinaryOp(left, op, right)

    def indicator(self, items):
        name = str(items[0])
        args = [Series(str(items[1])), items[2]]
        return Indicator(name, args)

    def NAME(self, token):
        return str(token)

    def NUMBER(self, token):
        return int(token)

parser = Lark(grammar, parser="lalr", transformer=DSLTransformer())
