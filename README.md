# Cryptocurrency Volatility Prediction

## 🚀 Project Overview
Cryptocurrency markets are highly volatile, and forecasting this volatility is critical for risk management, portfolio allocation, and trading strategies[cite: 1]. This project implements an end-to-end machine learning pipeline to predict cryptocurrency volatility levels based on historical market data including OHLC prices, trading volume, and market capitalization[cite: 1].

## 🛠️ Features & Methodology
* **Data Preprocessing & Consistency:** Handles missing values and normalizes numerical features[cite: 1].
* **Advanced Feature Engineering:** Calculates moving averages, rolling volatility, liquidity ratios (volume-to-market cap), and technical indicators like Bollinger Bands and Average True Range (ATR)[cite: 1].
* **Machine Learning Model:** Trains an XGBoost Regressor to anticipate market volatility variations.
* **Model Evaluation:** Assesses performance using standard metrics such as RMSE, MAE, and $R^2$ score[cite: 1].
* **Interactive Deployment:** Includes a local web interface built with Streamlit for testing predictions in real-time[cite: 1].

## 📂 Project Structure
* `crypto_data.csv`: Historical daily records for cryptocurrencies (price, volume, market cap)[cite: 1].
* `utils.py`: Data cleaning, preprocessing, and technical indicator generation script.
* `train.py`: Model training script that evaluates performance and saves the trained artifact.
* `app.py`: Streamlit dashboard for local deployment and interactive testing[cite: 1].
* `requirements.txt`: Required Python dependencies.

