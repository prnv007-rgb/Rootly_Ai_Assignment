import re

def parse_nl(text: str):
    text = text.lower()

    entry = []
    exit_ = []

    # close > SMA(close, 20)
    sma_match = re.search(r'close.*above.*(\d+)[- ]day moving average', text)
    if sma_match:
        period = int(sma_match.group(1))
        entry.append({
            "left": "close",
            "op": ">",
            "right": f"sma(close,{period})"
        })

    # volume > 1 million
    vol_match = re.search(r'volume.*above.*(\d+)\s*(million)?', text)
    if vol_match:
        val = int(vol_match.group(1))
        if vol_match.group(2):
            val *= 1_000_000
        entry.append({
            "left": "volume",
            "op": ">",
            "right": val
        })

    # exit RSI
    rsi_match = re.search(r'rsi.*below.*(\d+)', text)
    if rsi_match:
        exit_.append({
            "left": "rsi(close,14)",
            "op": "<",
            "right": int(rsi_match.group(1))
        })

    return {"entry": entry, "exit": exit_}
