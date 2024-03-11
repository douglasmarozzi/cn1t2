import streamlit as st
import plotly.graph_objs as go
import yfinance as yf

# Lista de bolsas disponíveis
bolsas_disponiveis = ["B3", "NASDAQ", "NYSE"]

# Perguntar ao usuário a bolsa e o nome da ação, data inicial e data final e plotar o gráfico do preço da ação no final do dia
st.text('Selecione a bolsa e insira o nome da ação')
bolsa = st.selectbox('Bolsa', bolsas_disponiveis)
acao = st.text_input('Ação') + f'.{bolsa}'

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
    # Printar o dataframe
    st.write(acao)
