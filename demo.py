import pandas as pd
import numpy as np

from n1_parser import parse_nl
from dsl_parser import parser
from codegen import eval_node
from backtest import backtest


# -----------------------------
# Synthetic Data Generator
# -----------------------------
def generate_sample_data(n=60, seed=42):
    np.random.seed(seed)

    dates = pd.date_range("2023-01-01", periods=n)
    price = np.cumsum(np.random.randn(n)) + 100

    df = pd.DataFrame({
        "date": dates,
        "open": price + np.random.randn(n),
        "high": price + np.random.rand(n) * 2,
        "low": price - np.random.rand(n) * 2,
        "close": price,
        "volume": np.random.randint(500_000, 2_000_000, size=n)
    })

    return df


# -----------------------------
# Natural Language Input
# -----------------------------
nl = (
    "Buy when the close price is above the 20-day moving average "
    "and volume is above 1 million. Exit when RSI is below 30."
)

structured = parse_nl(nl)

# -----------------------------
# Generated DSL (from NL)
# -----------------------------
dsl = """
ENTRY:
close > sma(close,20) AND volume > 1000000
EXIT:
rsi(close,14) < 30
"""

# -----------------------------
# Parse DSL → AST
# -----------------------------
ast_entry = parser.parse("close > sma(close,20)")
ast_exit = parser.parse("rsi(close,14) < 40")


# -----------------------------
# Generate Synthetic Data
# -----------------------------
df = generate_sample_data(n=80)

# -----------------------------
# Evaluate Signals
# -----------------------------
entry_signal = eval_node(ast_entry, df)
exit_signal = eval_node(ast_exit, df)

# -----------------------------
# Run Backtest
# -----------------------------
trades = backtest(df, entry_signal, exit_signal)

print("\nNatural Language Input:")
print(nl)

print("\nGenerated DSL:")
print(dsl)

print("\nBacktest Trades:")
for t in trades:
    print(t)
