import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Cryptocurrency Volatility Predictor', page_icon='📈', layout='wide'
)

st.title('🚀 Cryptocurrency Volatility Prediction Dashboard')
st.markdown(
    'This application predicts the future volatility level of cryptocurrencies'
    ' based on market indicators[cite: 1].'
)


@st.cache_resource
def load_model():
  try:
    return joblib.load('crypto_volatility_model.pkl')
  except:
    return None


model = load_model()

st.sidebar.header('Input Market Parameters')

open_p = st.sidebar.number_input('Open Price', value=100.0)
high_p = st.sidebar.number_input('High Price', value=105.0)
low_p = st.sidebar.number_input('Low Price', value=95.0)
close_p = st.sidebar.number_input('Close Price', value=102.0)
volume = st.sidebar.number_input('Trading Volume', value=1000000.0)
marketCap = st.sidebar.number_input('Market Capitalization', value=50000000.0)
returns = st.sidebar.number_input('Daily Returns', value=0.01)
rolling_vol = st.sidebar.number_input('Current Rolling Volatility', value=0.02)
liquidity_ratio = volume / (marketCap + 1e-8)


if st.sidebar.button('Predict Volatility'):
  if model is None:
    st.error(
        "Model file not found! Please run 'train.py' first to train and save"
        ' the model.'
    )
  else:
    input_data = pd.DataFrame(
        [[
            open_p,
            high_p,
            low_p,
            close_p,
            volume,
            marketCap,
            returns,
            rolling_vol,
            liquidity_ratio,
            
        ]],
        columns=[
            'open',
            'high',
            'low',
            'close',
            'volume',
            'marketCap',
            'returns',
            'rolling_volatility',
            'liquidity_ratio',
            
        ],
    )

    prediction = model.predict(input_data)
    st.success(
        f'Predicted Future Volatility Level: **{prediction[0]:.6f}**'
    )