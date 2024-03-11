import streamlit as st
import plotly.graph_objs as go
import yfinance as yf

def main():
    # Lista de bolsas disponíveis
    bolsas_disponiveis = ["B3", "NASDAQ", "NYSE"]

    # Perguntar ao usuário a bolsa e o nome da ação, data inicial e data final e plotar o gráfico do preço da ação no final do dia
    st.sidebar.header('Configurações')
    bolsa = st.sidebar.selectbox('Bolsa', bolsas_disponiveis)
    acao = st.sidebar.text_input('Ação')

    st.sidebar.text('Insira a data inicial')
    data_inicial = st.sidebar.date_input('Data Inicial')

    st.sidebar.text('Insira a data final')
    data_final = st.sidebar.date_input('Data Final')

    b1 = st.sidebar.button('Buscar')
    if b1:
        acao = yf.download(f"{acao}.{bolsa}", start=data_inicial, end=data_final)
        fig = go.Figure(data=[go.Candlestick(x=acao.index,
                                             open=acao['Open'],
                                             high=acao['High'],
                                             low=acao['Low'],
                                             close=acao['Close'])])

        st.plotly_chart(fig)
        # Printar o dataframe
        st.write(acao)

if __name__ == "__main__":
    main()
