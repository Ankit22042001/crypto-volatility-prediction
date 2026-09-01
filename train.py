import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from utils import load_and_preprocess_data


def train_model(file_path):
  print("Loading and preprocessing data...")
  df = load_and_preprocess_data(file_path)

  features = [
      'open',
      'high',
      'low',
      'close',
      'volume',
      'marketCap',
      'returns',
      'rolling_volatility',
      'liquidity_ratio',
      
  ]
  target = 'target_volatility'

  X = df[features]
  y = df[target]

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  print("Training XGBoost Regressor...")
  model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
  model.fit(X_train, y_train)

  predictions = model.predict(X_test)

  rmse = np.sqrt(mean_squared_error(y_test, predictions))
  mae = mean_absolute_error(y_test, predictions)
  r2 = r2_score(y_test, predictions)

  print("Model Evaluation Metrics:")
  print(f"RMSE: {rmse:.4f}")
  print(f"MAE: {mae:.4f}")
  print(f"R2 Score: {r2:.4f}")

  # Model save karna
  joblib.dump(model, 'crypto_volatility_model.pkl')
  print("Model saved successfully as 'crypto_volatility_model.pkl'.")


if __name__ == "__main__":
  # Apni CSV file ka naam yahan dein
  train_model("crypto_data.csv") 