import streamlit as st
import pandas as pd
import numpy as np
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

st.title('Portfolio Optimization')

# Function to invert text
def inverter_texto(texto):
    return texto[::-1]

# Dictionary containing stock exchanges and their corresponding codes
stock_exchanges = {
    'Bovespa (Brazil)': 'SAO',
    'New York Stock Exchange (USA)': 'NYQ',
    'NASDAQ (USA)': 'NAS',
    'London Stock Exchange (UK)': 'LON',
    # Add more exchanges if needed
}

st.text('Escolha a bolsa de valores:')
selected_exchange = st.selectbox('Bolsa', list(stock_exchanges.keys()))

# Input form for assets and expected returns
st.sidebar.header('Input Parameters')

# Number of assets in the portfolio
num_assets = st.sidebar.number_input('Number of Assets', min_value=2, max_value=10, value=5)

# Expected returns for each asset
expected_returns = {}
for i in range(num_assets):
    asset_name = st.sidebar.text_input(f'Asset {i+1} Name', value=f'Asset {i+1}')
    expected_return = st.sidebar.number_input(f'Expected Return for {asset_name}', min_value=0.0, value=0.05, step=0.01)
    expected_returns[asset_name] = expected_return

# Generate DataFrame of expected returns
df_expected_returns = pd.DataFrame.from_dict(expected_returns, orient='index', columns=['Expected Return'])

# Display expected returns DataFrame
st.write('### Expected Returns')
st.write(df_expected_returns)

# Portfolio Optimization
if st.button('Optimize Portfolio'):
    # Calculate expected returns and sample covariance
    mu = expected_returns = expected_returns(df_expected_returns)
    S = risk_models.sample_cov(df_expected_returns)

    # Optimize portfolio for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S)
    raw_weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()

    # Display optimized weights
    st.write('### Optimized Portfolio Weights')
    st.write(pd.Series(cleaned_weights))

    # Calculate expected return, volatility, and Sharpe ratio
    expected_return, volatility, sharpe_ratio = ef.portfolio_performance()
    st.write(f'Expected Portfolio Return: {expected_return}')
    st.write(f'Portfolio Volatility: {volatility}')
    st.write(f'Sharpe Ratio: {sharpe_ratio}')
