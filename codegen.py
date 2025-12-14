from ast_nodes import Series, Indicator, BinaryOp
from indicators import sma, rsi


def eval_node(node, df):

    # -----------------------------
    # Literal constant (numbers)
    # -----------------------------
    if isinstance(node, (int, float)):
        return node

    # -----------------------------
    # Column reference
    # -----------------------------
    if isinstance(node, Series):
        return df[node.name]

    # -----------------------------
    # Indicator computation
    # -----------------------------
    if isinstance(node, Indicator):
        if node.name == "sma":
            series_name = node.args[0].name
            period = node.args[1]
            return sma(df[series_name], period)

        if node.name == "rsi":
            series_name = node.args[0].name
            period = node.args[1]
            return rsi(df[series_name], period)

        raise ValueError(f"Unknown indicator: {node.name}")

    # -----------------------------
    # Binary operation
    # -----------------------------
    if isinstance(node, BinaryOp):
        left = eval_node(node.left, df)
        right = eval_node(node.right, df)

        if node.op == ">":
            return left > right
        if node.op == "<":
            return left < right
        if node.op == ">=":
            return left >= right
        if node.op == "<=":
            return left <= right
        if node.op == "==":
            return left == right

        raise ValueError(f"Unknown operator: {node.op}")

    raise TypeError(f"Unknown AST node type: {type(node)}")
