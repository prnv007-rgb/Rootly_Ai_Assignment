class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Indicator:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Series:
    def __init__(self, name):
        self.name = name
