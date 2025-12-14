import pandas as pd
import numpy as np

def generate_sample_data(n=60):
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
