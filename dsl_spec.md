ENTRY:
close > sma(close,20) AND volume > 1000000

EXIT:
rsi(close,14) < 30
