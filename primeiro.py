import streamlit as st
import plotly.graph_objs as go
import yfinance as yf

st.title('Hello World')

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

st.text('Insira o nome da ação')
acao = st.text_input('Ação') + '.' + stock_exchanges[selected_exchange]

st.text('Insira a data inicial')
data_inicial = st.date_input('Data Inicial')

st.text('Insira a data final')
data_final = st.date_input('Data Final')

b1 = st.button('Buscar')
if b1:
    acao = yf.download(acao, start=data_inicial, end=data_final)
    fig = go.Figure(data=[go.Candlestick(x=acao.index,
                                         open=acao['Open'],
                                         high=acao['High'],
                                         low=acao['Low'],
                                         close=acao['Close'])])

    st.plotly_chart(fig)
    # Print the dataframe
    st.write(acao)
