import pandas as pd
from utils import create_binance_client
from strategy import apply_strategy

def fetch_klines(client, symbol='BTCUSDT', interval='1m', limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    df['close'] = df['close'].astype(float)
    return df

def main():
    print("Iniciando bot de simulação...")
    client = create_binance_client()

    df = fetch_klines(client)
    signal = apply_strategy(df)

    if signal == 'buy':
        print("📈 Sinal de COMPRA detectado.")
    elif signal == 'sell':
        print("📉 Sinal de VENDA detectado.")
    else:
        print("⏸ Nenhum sinal claro. Aguardar...")

if __name__ == "__main__":
    main()
