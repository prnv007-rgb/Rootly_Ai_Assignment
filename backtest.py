def backtest(df, entry_signal, exit_signal):
    in_position = False
    trades = []
    entry_price = None

    for i, row in df.iterrows():
        if entry_signal[i] and not in_position:
            in_position = True
            entry_price = row['close']
            entry_date = row['date']

        elif exit_signal[i] and in_position:
            in_position = False
            exit_price = row['close']
            trades.append({
                "entry_date": entry_date,
                "exit_date": row['date'],
                "pnl": exit_price - entry_price
            })

    return trades
