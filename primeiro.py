import streamlit as st
import plotly.graph_objs as go
import yfinance as yf

st.title('Hello World')

st.text('Inseria seu nome')
nome = st.text_input('Nome')

st.write(f'Olá {nome}')

def inverter_texto(texto):
    return texto[::-1]


nome_invertido = inverter_texto(nome)
st.write(f'Seu nome invertido é {nome_invertido}')

# perguntar ao usuario o nome da ação, data inicial e data final e plotar o grafico do preço da ação no final do dia
st.text('Insira o nome da ação')
acao = st.text_input('Ação') + '.SA'

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
    # printar o dataframe
    st.write(acao)
