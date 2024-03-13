import streamlit as st
import pandas as pd
import numpy as np
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

st.title('Otimização de Carteira de Investimentos')

# Função para inverter texto
def inverter_texto(texto):
    return texto[::-1]

# Dicionário contendo bolsas de valores e seus códigos correspondentes
bolsas_valores = {
    'Bovespa (Brasil)': 'SAO',
    'Bolsa de Valores de Nova York (EUA)': 'NYQ',
    'NASDAQ (EUA)': 'NAS',
    'Bolsa de Valores de Londres (Reino Unido)': 'LON',
    # Adicione mais bolsas se necessário
}

st.text('Escolha a bolsa de valores:')
bolsa_selecionada = st.selectbox('Bolsa', list(bolsas_valores.keys()))

# Formulário de entrada para ativos e retornos esperados
st.sidebar.header('Parâmetros de Entrada')

# Número de ativos na carteira
num_ativos = st.sidebar.number_input('Número de Ativos', min_value=2, max_value=10, value=5)

# Retornos esperados para cada ativo
retornos_esperados = {}
for i in range(num_ativos):
    nome_ativo = st.sidebar.text_input(f'Nome do Ativo {i+1}', value=f'Ativo {i+1}')
    retorno_esperado = st.sidebar.number_input(f'Retorno Esperado para {nome_ativo}', min_value=0.0, value=0.05, step=0.01)
    retornos_esperados[nome_ativo] = retorno_esperado

# Gerar DataFrame de retornos esperados
df_retornos_esperados = pd.DataFrame.from_dict(retornos_esperados, orient='index', columns=['Retorno Esperado'])

# Exibir DataFrame de retornos esperados
st.write('### Retornos Esperados')
st.write(df_retornos_esperados)

# Otimização de Carteira
if st.button('Otimizar Carteira'):
    # Calcular retornos esperados e covariância amostral
    mu = expected_returns = expected_returns(df_retornos_esperados)
    S = risk_models.sample_cov(df_retornos_esperados)

    # Otimizar carteira para maximizar o índice de Sharpe
    ef = EfficientFrontier(mu, S)
    pesos_raw = ef.max_sharpe()
    pesos_limpos = ef.clean_weights()

    # Exibir pesos otimizados
    st.write('### Pesos da Carteira Otimizada')
    st.write(pd.Series(pesos_limpos))

    # Calcular retorno esperado, volatilidade e índice de Sharpe
    retorno_esperado, volatilidade, indice_sharpe = ef.portfolio_performance()
    st.write(f'Retorno Esperado da Carteira: {retorno_esperado}')
    st.write(f'Volatilidade da Carteira: {volatilidade}')
    st.write(f'Índice de Sharpe: {indice_sharpe}')
