
@@ -2,23 +2,13 @@
importar  plotadamente . graph_objs  em  andamento
importar  yfinance  como  yf

st . título ( 'Olá mundo' )
# Lista de bolsas disponíveis
bolsas_disponiveis  = [ "B3" , "NASDAQ" , "NYSE" ]

st . text ( 'Inseria seu nome' )
nome  =  st . text_input ( 'Nome' )

st . escreva ( f'Olá { nome } ' )

def  inversor_texto ( texto ):
    retornar  texto [:: - 1 ]


nome_invertido  =  inverter_texto ( nome )
st . write ( f'Seu nome invertido é { nome_invertido } ' )

# perguntar ao usuário o nome da ação, dados iniciais e dados finais e plotar o gráfico do preço da ação no final do dia
st . text ( 'Insira o nome da ação' )
acao  =  st . text_input ( 'Ação' ) +  '.SA'
# Pergunte ao usuário a bolsa e o nome da ação, dados iniciais e dados finais e plotar o gráfico do preço da ação no final do dia
st . text ( 'Selecione a bolsa e insira o nome da ação' )
bolsa  =  st . selectbox ( 'Bolsa' , bolsas_disponiveis )
acao  =  st . text_input ( 'Ação' ) +  f'. { bolsa } '

st . text ( 'Insira os dados iniciais' )
dados_inicial  =  st . data_input ( 'Dados Iniciais' )
@@ -30,11 +20,11 @@ def inverter_texto(texto):
se  b1 :
    acao  =  yf . baixar ( acao , início = dados_inicial , fim = dados_final )
    figo  =  vai . Figura ( dados = [ go . Candlestick ( x = acao . index ,
                                      open = acao [ 'Abrir' ],
                                      alto = acao [ 'Alto' ],
                                      baixo = acao [ 'Baixo' ],
                                      fechar = acao [ 'Fechar' ])])
                                         open = acao [ 'Abrir' ],
                                         alto = acao [ 'Alto' ],
                                         baixo = acao [ 'Baixo' ],
                                         fechar = acao [ 'Fechar' ])])

    st . plotly_chart ( fig )
    #imprime o dataframe
    # Imprimir o dataframe
    st . escreva ( açao )
