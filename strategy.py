import pandas as pd
import ta

def apply_strategy(df):
    df['sma_short'] = ta.trend.sma_indicator(df['close'], window=5)
    df['sma_long'] = ta.trend.sma_indicator(df['close'], window=20)

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    if previous['sma_short'] < previous['sma_long'] and latest['sma_short'] > latest['sma_long']:
        return 'buy'
    elif previous['sma_short'] > previous['sma_long'] and latest['sma_short'] < latest['sma_long']:
        return 'sell'
    else:
        return 'hold'
