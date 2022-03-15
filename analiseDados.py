import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

# Removendo coluna (ou linha) da tabela

tabela = tabela.drop("Unnamed: 0",axis = 1) # axis = 0 -> linha, axis = 1 -> coluna

# Verificando se os dados ta tabela estão sendo lidas corretamente

# transformando os dados de uma coluna que esta errado para o tipo de dado correto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = 'coerce') # coerce = deixar vazio em caso de erro


# Excluindo colunas que nao possuem dados (vazias)

tabela = tabela.dropna(how="all",axis= 1)

# Excluindo linhas que possuem pelo menos uma informaçao vazia

tabela = tabela.dropna(how="any",axis= 0)

# print(tabela.info())

# Quantos clientes cancelaram? (26%)

print(tabela["Churn"].value_counts()) # retorna a quantidade de clientes que cancelaram

print(tabela["Churn"].value_counts(normalize = True).map("{:.1%}".format)) # normalize = True -> retorna a porcentagem de clientes que cancelaram

# Cria grafico
# https://plotly.com/python/histograms/

for coluna in tabela.columns:

    grafico = px.histogram(tabela, x = coluna,color = "Churn") # x = coluna, color = coluna que vai ser usada para colorir o grafico
    grafico.show()