import pandas as pd
import numpy as np


def compute_rsi(series, window=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def add_technical_indicators(df):
    # Ensure Close is float
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # RSI
    df['RSI'] = compute_rsi(df['Close'])

    # MACD and Signal
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    # Bollinger Bands
    rolling_mean = df['Close'].rolling(window=20).mean()
    rolling_std = df['Close'].rolling(window=20).std()
    df['Bollinger Upper'] = rolling_mean + (2 * rolling_std)
    df['Bollinger Lower'] = rolling_mean - (2 * rolling_std)

    return df


def add_target_label(df):
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    return df


def preprocess_features(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df = df[1:]  # Skip header issue if needed
    df.set_index('Date', inplace=True)

    # Convert all to numeric
    for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Add daily return
    df['Daily Return'] = df['Close'].pct_change()

    df = add_technical_indicators(df)
    df = add_target_label(df)
    df.dropna(inplace=True)
    return df