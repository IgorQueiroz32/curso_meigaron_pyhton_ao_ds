# curso de python, seja um data scientist
# aula 1

# problema de negocio
# planejamento de solucao
# o que e python?
# como escrevr em python?
# primeiros comandos em python
# responder questoes de negocio


# 1 problema de negocio

# https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/

# empresa = house rocket - plataforma de compra e venda de imoveis

# 1.1 problema da empresa - maximizaer o lucro daempresa encontrando bons negocios
# 1.2 estrategia - fontes externas para encontrar bons negocios
# 1.3 perguntas - qunatas casas estao disponiveis para compra?
#           - quantos atributos as casas possuem ( numero de quartos, numero de garagens, m2, vista pro mar)?
#           - quais sao os atributos?
#           - qual casa mais cara?
#           - qual a casa com o maior numero de quartos?

# 2 planejamento da solucao

# 2.1 planejamento do produto final 

# o q entregar? (planilha, texro, email, modelo de ml,...) R: texto com respostas
# como vai ser a entrega? R: perguntas / respostas
# Exemplo:  - qunatas casas estao disponiveis para compra? R: 2300 imoveis disponiveis para compra
#           - quantos atributos as casas possuem ( numero de quartos, numero de garagens, m2, vista pro mar)? R: 10 tributos
#           - quais sao os atributos? 
#           - qual casa mais cara?
#           - qual a casa com o maior numero de quartos?

# 2.2 Planejamento do processo 

# onde esta a informacao? (excell, Bd, API, manual) R: kaggle em csv
# como coletar? (sql, python) R: python
#responder as perguntas -  - qunatas casas estao disponiveis para compra? R: contar o numero de linhas do conjunto de dados
#           - quantos atributos as casas possuem ( numero de quartos, numero de garagens, m2, vista pro mar)? R: contar o numero de colunas do dataset
#           - quais sao os atributos? R: mostrar os nomes da colunas de forma automatica
#           - qual casa mais cara? R: ordenar as linhas pela coluna de preco
#           - qual a casa com o maior numero de quartos? R: ordenar as linhas pelo coluna numero de quartos


# 2.3 planejamento das ferramentas

# quais ferramenta eu posso usar? (excel, Python, R) R: python - processar e manipular -> insights

# 3 o que e python?

#linguagem de programacao - 

# exemplo de codificacao do python

# pessoa -> comando verbal /visual -> objeto ->  realizar acao  -> visualizacao do comando feito
# Igor -> "senta" -> cachoro -> sentar -> cachorro sentado

# traduzindo para programacao

#pessoa -> comando escrito -> computador -> realiza a acao -> mostra resultado
#pessoa -> comando escrito -> compilador/interpretador -> linguagem de maquina (binario) -> processador -> executar a acao -> mostra resultado

# exemplo de comando

# Igor - "selecione 2 colunas"
# Igor - "data[[X,Y]]

# Igor "ordena as linhas do dataset pela coluna z"
# Igor - "data.sort_values(Z)"

# Igor "ordena as linhas do dataset pela coluna z de forma crescente"
# Igor - "data.sort_values(Z,ascending=True)"



# Pra responder perguntas do CEO

#            Igor -> contar o numero de linhas do conjunto de dados
#            Igor -> contar o numero de colunas do dataset
#            Igor -> mostrar os nomes da colunas de forma automatica
#            Igor -> ordenar as linhas pela coluna de preco (atributos)
#            Igor -> ordenar as linhas pelo coluna numero de quartos (atributos)


# 4 como escrevr em python?

# Editor de texto -  bloco de notas, gedit, textEdit
# interpretador (comandos -> linguagem de maquina (binario) -> processador) ex: python 3.x

#IDE(intaerface development environment)EX: PyCharm, Spyder, VSCode, JUPYRT laB

# 5 Os primeiros comandos em Python

#executar o processo

# onde esta a informacao? (excell, Bd, API, manual) R: kaggle em csv
# como coletar? (sql, python) R: python
# Pra responder perguntas do CEO

#            Igor -> contar o numero de linhas do conjunto de dados
#            Igor -> contar o numero de colunas do dataset
#            Igor -> mostrar os nomes da colunas de forma automatica
#            Igor -> ordenar as linhas pela coluna de preco (atributos)
#            Igor -> ordenar as linhas pelo coluna numero de quartos (atributos)

# Como eu sei qual o comando para contar o numero de linhas?


# 5.1 estrutura do comando

# humano -> comando escreito -> computador -> realizar uam acao -> mostrar um resultado

# Como fazer bolo de chocolate 

#ingredientes: ovos, leite, etc
#modo de preparo: bata liquidificaor, leve ao forno , etc

# modo de preparo -> manipula -> ingredientes -> bolo de chocolate

# quero abrir uma loja de bolo e ensinar para outras pessoas como fazer bolo

# R: ingerdientes + modo de preparo = receita

#quer abrir uma loja de bolo e ensinar para outras pessoas como fazer tudo
#Bolo de chocolate
#churros
#Doces

# R: receita de bolo + receita de doces = livro de receitas


# RESUMINDO

# livro de receita   organiza   receitas
# Receita            replica    modo de preparo
# Modo de preparo    manipula   ingredientes


# EM PROGRAMACAO:

# biblioteca  organiza   Funcoes
# Funcoes     replica    Comandos 
# Comandos    manipula   Variaveis


# Ex:  pessoa -> comando escrito -> computador -> realiza a acao -> mostra resultado
#      pessoa -> comando escrito -> compilador/interpretador -> linguagem de maquina (binario) -> processador -> executar a acao -> mostra resultado


# 5.2 Estruturas

# EM PROGRAMACAO:

# biblioteca  organiza   Funcoes
# Funcoes     replica    Comandos 
# Comandos    manipula   Variaveis


# Variavies:
# - caixa armazenadora
# - tem nome
# - guarda um tipo de objeto
# - nao guarda objetos diferentes ao mesmo tempo

#Exemplo:
# caixa armazenadora
# - nome: caixa_calcas
# - armazeno: calcas

# - posso guardar sapatos dentro da caixa-clacas? nao
# - posso guardar saia dentro da caixa-calcas? nao

#em programacao:
# - caixa armazenadora e um espaco de memoria q guarda objeto
# - nome/tipo (nao usa dialetos latinos(~), nao usa espaco)


# Funcoes:
# -  sequencia de comandos
# - tem um nome
# - pode ou nao receber parametros de entrada
# - pode ou nao retornar parametros de saida
# - o que acontece na funcao, fica na fincao



#em programacao:
# - A funcao e uma sequencia de comandos
# - O nome da funcao tem q ser o mais proximo de sua responsabilidade
# - funcao ela pode ou nao receber/retornar valores


# Bibioteca
# - a biblioteca e um agrupamento de funcoes
# -  pode ter um apelido
# - precisa ser importado


# Exemplo de comados:

# mostre na tela a frase " Hello World"
print("Hello World")

# mostre na tela o resultado da soma de 30 + 50
print(30+50)

soma_de_numeros = 30 + 50
# na programacao o = e um operador de atribuicao, onde o redultado da conta e armazenado dentro da variavel

# mostre o conteudo da variavel soma_de_numeros
print(soma_de_numeros)


# carregue o conjunto de dados chamado kc_house_data.csv do hd para a memoria
# comando -> carregue o conjunto de arquivos
# funcao -> read_csv
# biblioteca -> pandas
# variavel -> data
# para instalar o pandas -> "pip install pandas" no prompt de comando do anaconda
import pandas as pd
data = pd.read_csv('kc_house_data.csv')

# mostre as primeiras linhas do conjunto de dados

print(data.head())

# mostre o numero de colunas e nomero de linhas do dataset

print(data.shape)


# mostre na tela o nome das colunas dos datasets

print(data.columns)

#mostre na tela o dataset ordenado pela coluna price

print(data.sort_values('price')) # este comando mostra todas as colunas do dataset

# para ver somente a coluna preco e outra desejada usa-se segunte funcao

print(data[['id','price']].sort_values('price'))

#mostre na tela o dataset ordenado pela coluna price do maior ao menor

print(data[['id','price']].sort_values('price', ascending=False))

#Exercicio: responder as questoes do CEO


#           - qunatas casas estao disponiveis para compra?
#           - quantos atributos as casas possuem ( numero de quartos, numero de garagens, m2, vista pro mar)?
#           - quais sao os atributos?
#           - qual casa mais cara?
#           - qual a casa com o maior numero de quartos?


#            Igor -> contar o numero de linhas do conjunto de dados
#            Igor -> contar o numero de colunas do dataset
#            Igor -> mostrar os nomes da colunas de forma automatica
#            Igor -> ordenar as linhas pela coluna de preco (atributos)
#            Igor -> ordenar as linhas pelo coluna numero de quartos (atributos)


# qual a soma total de quartos do conjunto de dados?
# qunatas casas possuem 2 banheiros?
# qual o preco medio de todas as casas no conjunto de dados?
# qual e o preco medio de casa com 2 banheiros?
# qual o preco minimo entre as casas com 3 quartos?
# quantas casas possuem mais de 300 metros quadadros na sala de estar?
# quantas casas tem amis de 2 andares?
# quantas casas tem vista para o mar?
# Das casas com vista para o mar, quntas tem 3 quartos?
# Das casas com mais de 300 metros quadrados de sala de estar, quanta tem 2 banheiros?


# Respostas

# quantas casas estao disponiveis para compra?
print(data.shape)
# R: 21613 linhas, logo 21613 casas

# quantos atributos as casas possuem ( numero de quartos, numero de garagens, m2, vista pro mar)?
print(data.shape)
# R: 21 colunas, logo 21 atributos

# quais sao os atributos?
print(data.columns)
# R: 'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
# 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15'

# qual casa mais cara?
print(data[['id','price']].sort_values('price', ascending=False))
# R: numero de index = 7252, numero de id = 6762700020, valor = 7700000.0

# qual a casa com o maior numero de quartos?
print(data[['id','bedrooms']].sort_values('bedrooms', ascending=False))
# R: numero de index = 15870, numero de id = 2402100895, numero de quartos = 33

# qual a soma total de quartos do conjunto de dados?
print(data['bedrooms'].sum())
# R: 72854 quartos

# qunatas casas possuem 2 banheiros?
print(data[['id', 'bathrooms']][data['bathrooms']==2])
# R: 1930 casas possuem 2 banheiros

# qual o preco medio de todas as casas no conjunto de dados?
print(data['price'].mean())
# R: O preco medio de todas as casas e de 540088.1417665294

# qual e o preco medio de casa com 2 banheiros?
two_bathrooms_house = data[['id', 'bathrooms', 'price']][data['bathrooms']==2]
print(two_bathrooms_house['price'].mean())

print( data.loc[data['bathrooms'] == 2, 'price'].mean() )
# R: O preco medio de todas as casas com 2 banheiros e de 457889.7186528497

# qual o preco minimo entre as casas com 3 quartos?
three_bedrooms_house = data[['id', 'bedrooms', 'price']].loc[data['bedrooms']==3]
print(three_bedrooms_house[['id','price']].sort_values('price', ascending=True))

print(data.loc[data['bedrooms']==3,'price'].min())
# R: O preco minimo das casas com 3 quartis e de 82000.0

# quantas casas possuem mais de 300 metros quadadros na sala de estar? 300 m2 = 3229.17 sqft
print(data[['id', 'sqft_living']][data['sqft_living']>3229.17])
# R: Existem 2258 casas com mais de 300 metros quadrados de sala de estar

# quantas casas tem amis de 2 andares?
print(data[['id', 'floors']][data['floors']>2])
# R: Existem 782 casas com mais de 2 andares

# quantas casas tem vista para o mar?
print(data[['id', 'waterfront']][data['waterfront']==1])
# R: Existem 163 casas com vista para o mar

# Das casas com vista para o mar, quntas tem 3 quartos?
three_bedrooms_house_waterfront = data[['id', 'waterfront', 'bedrooms']][data['waterfront']==1]
print(three_bedrooms_house_waterfront[['id', 'bedrooms']][three_bedrooms_house_waterfront['bedrooms']==3])


print( data[(data['waterfront'] == 1 ) & ( data['bedrooms'] == 3 )].shape )
# R: Existem 64 casas com vista para o mar e 3 quartos

# Das casas com mais de 300 metros quadrados de sala de estar, quanta tem 2 banheiros? 300 m2 = 3229.17 sqft
data2 = data[['id', 'sqft_living', 'bathrooms']][data['sqft_living']>3229.17]
print(data2[['id', 'bathrooms']][data2['bathrooms']==2])

print(data[(data['bathrooms']==2) & (data['sqft_living']>3229.17)])
# R: Existem 18 casas com mais de 300 metros quadrados de sala de estar e 2 banheiros

#### .loc so e utilizado quando se quer fazer alguma conta com os atributos

##aki nao utiliza
## por exemplo: quando se quer saber quantas casas tem 2 andares, nao se usa o .loc, print(data[data['floors']>2])

## aki utiliza
### mas quando se quer saber a media de preco para casas de 2 banheiros, print( data.loc[data['bathrooms'] == 2, 'price'].mean() )
### ou o preco minimo para casas de 3 quartos, print(data.loc[data['bedrooms']==3,'price'].min())


