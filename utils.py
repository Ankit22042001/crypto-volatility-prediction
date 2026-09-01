<<<<<<< HEAD
import numpy as np
import pandas as pd


def load_and_preprocess_data(file_path):
  # Dataset load karein
  df = pd.read_csv(file_path)

  # Missing values handle karna
  df.ffill(inplace=True)
  df.bfill(inplace=True)

  # Date sort karna
  if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['crypto_name', 'date'])

  # Feature Engineering: Returns & Rolling Volatility
  df['returns'] = df.groupby('crypto_name')['close'].pct_change()
  df['rolling_volatility'] = (
      df.groupby('crypto_name')['returns'].rolling(window=7).std().reset_index(0, drop=True)
  )

  # Liquidity Ratio (Volume / Market Cap)
  df['liquidity_ratio'] = df['volume'] / (df['marketCap'] + 1e-8)

  # Technical Indicators: Bollinger Bands & ATR
  df['ma_20'] = df.groupby('crypto_name')['close'].rolling(window=20).mean().reset_index(0, drop=True)
  df['std_20'] = df.groupby('crypto_name')['close'].rolling(window=20).std().reset_index(0, drop=True)
  df['bollinger_upper'] = df['ma_20'] + (df['std_20'] * 2)
  df['bollinger_lower'] = df['ma_20'] - (df['std_20'] * 2)

  # Average True Range (ATR) calculation
  df['h_l'] = df['high'] - df['low']
  df['h_pc'] = abs(df['high'] - df['close'].shift(1))
  df['l_pc'] = abs(df['low'] - df['close'].shift(1))
  df['tr'] = df[['h_l', 'h_pc', 'l_pc']].max(axis=1)
  df['atr'] = df.groupby('crypto_name')['tr'].rolling(window=14).mean().reset_index(0, drop=True)

  # Target Variable: Next day volatility prediction
  df['target_volatility'] = df.groupby('crypto_name')['rolling_volatility'].shift(-1)

  df.dropna(inplace=True)
=======
import numpy as np
import pandas as pd


def load_and_preprocess_data(file_path):
  # Dataset load karein
  df = pd.read_csv(file_path)

  # Missing values handle karna
  df.ffill(inplace=True)
  df.bfill(inplace=True)

  # Date sort karna
  if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['crypto_name', 'date'])

  # Feature Engineering: Returns & Rolling Volatility
  df['returns'] = df.groupby('crypto_name')['close'].pct_change()
  df['rolling_volatility'] = (
      df.groupby('crypto_name')['returns'].rolling(window=7).std().reset_index(0, drop=True)
  )

  # Liquidity Ratio (Volume / Market Cap)
  df['liquidity_ratio'] = df['volume'] / (df['marketCap'] + 1e-8)

  # Technical Indicators: Bollinger Bands & ATR
  df['ma_20'] = df.groupby('crypto_name')['close'].rolling(window=20).mean().reset_index(0, drop=True)
  df['std_20'] = df.groupby('crypto_name')['close'].rolling(window=20).std().reset_index(0, drop=True)
  df['bollinger_upper'] = df['ma_20'] + (df['std_20'] * 2)
  df['bollinger_lower'] = df['ma_20'] - (df['std_20'] * 2)

  # Average True Range (ATR) calculation
  df['h_l'] = df['high'] - df['low']
  df['h_pc'] = abs(df['high'] - df['close'].shift(1))
  df['l_pc'] = abs(df['low'] - df['close'].shift(1))
  df['tr'] = df[['h_l', 'h_pc', 'l_pc']].max(axis=1)
  df['atr'] = df.groupby('crypto_name')['tr'].rolling(window=14).mean().reset_index(0, drop=True)

  # Target Variable: Next day volatility prediction
  df['target_volatility'] = df.groupby('crypto_name')['rolling_volatility'].shift(-1)

  df.dropna(inplace=True)
>>>>>>> 055edc2ad8c18d9809fb1f1d3fb2c96de18e89d1
  return df 