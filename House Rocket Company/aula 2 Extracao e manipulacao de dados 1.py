# 1 novas perguntas de negocio
# 2 planejamento da solucao
# 3 tipos de variaveis
# 4 manipulacao de variaveis
# 5 exercicios praticos

# 1 novas perguntas de negocio
# 1.1 recapitulando o desafio

# 1.2 novas perguntas do ceo

# qual a data do imovel mais antigo no portfolio?

# quantos imoveis possuem o numero maximo de andares?

# criar uma classificacao para imoveis, separando-os em baixo e alto padrao, de acordo com o preco. acima de 540.000 -> alto padrao
#                                                                                                   abaixo de 540.000 -> baixo padrao

# gostaria de um relatorio ordenado pelo preco e contendo as seguintes informacoes: 
# (id do imovel, 
# data q o imovel ficou disponivel para compra,
# o numeor de quartos,
# o tamanho total do terreno,
# o preco,
# a classificacao do imovel (alto e baixo))

# gostaria de um mapa indicando onde as casas estao localizadas geograficamente

# 2 planejamento da solucao

# 2.1 produto final ( o que entregar? planilha, email, grafico, modelo de ml...)

#  R: emaiil + 2 anexos:
# email: - texo : perguntas e respostas
# anexo: - um relatorio em .csv e a foto de um mapa em html

# 2.2 ferramenta ( qual ferramenta usar?)

# R: python e pycharm

# 2.3 processo ( como fazer?)

# qual a data do imovel mais antigo no portfolio? 

# R: ordenar o conjunto de dados pela menor data

# quantos imoveis possuem o numero maximo de andares?

# R: encontar o numero de andars e determinar o maior
#    contar quantos imoveis eu tenho por andar

# criar uma classificacao para imoveis, separando-os em baixo e alto padrao, de acordo com o preco. acima de 540.000 -> alto padrao (high_standard)
#                                                                                                  abaixo de 540.000 -> baixo padrao (low_standard)

# R: criar uma nova coluna no dataset e chamar de standard
#    para cada linha, comparar a coluna price
#    se price for maior que 540.000, escrever high_standard na coluna standard
#    se price for menor que 540.000, escrever low_standard na coluna standard
 
# gostaria de um relatorio ordenado pelo preco e contendo as seguintes informacoes: 
# (id do imovel, 
# data q o imovel ficou disponivel para compra,
# o numeor de quartos,
# o tamanho total do terreno,
# o preco,
# a classificacao do imovel (alto e baixo))

# R: selecionar as colunas desejadas/demandadas
#    deletar as colunas desejadas/demandadas                                                                                               

# gostaria de um mapa indicando onde as casas estao localizadas geograficamente 
                                                                                                  
# R:  procurar uma biblioteca em python q amrmazena uma funcao que desenha mapa.
#     aprender a user a funcao q desenha mapas    

# 3 tipos de variaveis
# - caixa armazenadora ( espaco de memoria)
# - precisa ter um nome e um tipo

# - boas praticas para o nome:
# - expressar a responsabilidade da variavel
# - seguir um estili (kamel case e snake case)
# - kamel case: HousePrice (as primeiras letras das palavras sao maiusculas) usado em orientacao objeto
# - snake case: house_price ( tudo minusculo separado por underline) mais utilizado

# - tipos das variavies em python:
# - numerica ( inteiro (valor sem virgula), float ( valor com virgula))
# -  categorica (caracters ex: "i" "g" "o" "r" ( letras), strings ex: "igor" (palavra))
# - dates ( date (ano-mes-dia); Timestamp (ano-nes-dia H-min-sec))

# - identificar os tipos das variaveis
# - comando dtypes

# exemplo no python

# carrea um arquivo do hd para memoria
# funcao: e uma sequencia de comandos  e recebe uma entrada e devolve uma saida (parametros de entrada -> um resultado)

import pandas as pd
data = pd.read_csv('kc_house_data.csv')

# mostra na tela as primeiras 6 linhas
print(data.head(6))

# mostra na tela os tipos de variaveis em cala coluna
print(data.dtypes)

# funcao q converte de object (string) para date
data['date'] = pd.to_datetime(data['date'])

print(data.head(6))

print(data.dtypes)

# como converter os tipos de variaveis

# inteiro -> float
data['bedrooms'] = data['bedrooms'].astype(float)
print(data.dtypes)
print(data[['id','bedrooms']].head(3))

# float -> inteiro # obs: ou todas as colunas sao int32 ou todas as colunas sao int64, nao pode ser misturado pois da erro
import numpy as np
data['bedrooms'] = data['bedrooms'].astype(np.int64)
print(data.dtypes)
print(data[['id','bedrooms']].head(3))

# inteiro -> string
data['bedrooms'] = data['bedrooms'].astype(str)
print(data.dtypes)
print(data[['id','bedrooms']].head(3))

# string -> inteiro
data['bedrooms'] = data['bedrooms'].astype(np.int64)
print(data.dtypes)
print(data[['id','bedrooms']].head(3))

# inteiro -> data
data['date'] = pd.to_datetime(data['date'])
print(data.head(6))
print(data.dtypes)

# 4 manipulacao de variaveis
# -  criar (colunas de variaceis e novas linhas)
# -  deletar (colunas de variaceis e novas linhas)
# -  selecionar (colunas de variaceis e novas linhas)

# 4.1 formas de selecionas dados:
# - forma 1: direto pelo nome das colunas
# - forma 2: Pelos indices das colunas
# - forma 3: pelos indices das linhas e pelo nome das colunas
# - forma 4: pelos indices booleanos. (true e False)


# criando novas variaveis
import pandas as pd
data = pd.read_csv('kc_house_data.csv')

# criando nova coluna

print(data.columns)

data['nome_do_igor'] = "igor"

print(data.columns)

print(data[['id','date','nome_do_igor']].head())

data['comunidade_ds'] = 100
print(data[['id','date','nome_do_igor','comunidade_ds']].head())

data['data_aula'] = pd.to_datetime('2021-03-03')
print(data[['id','date','nome_do_igor','comunidade_ds', 'data_aula']].head())
print(data.dtypes)


# deletar variaveis

print(data.columns)
data = data.drop('nome_do_igor', axis=1)
data = data.drop(['comunidade_ds', 'data_aula'], axis=1)

print(data.columns)                                                                                          
                       
#ou

cols = ['comunidade_ds', 'data_aula']                                                                           
data = data.drop(cols, axis=1)                                                                                                
print(data.columns)  

# selecionar dados
# - forma 1: direto pelo nome das colunas

print(data['id'])
print(data[['price','date']])

# - forma 2: Pelos indices das linhas e colunas
# quando nao sabemos o nome das colunas usamos uma funcao chamada iloc (localiza pelo index) para achar o nome e as linhas das colunas desejadas
#dados [linhas, colunas]
print(data.iloc[0:10, 0:3])
#para achar todas as linhas ou/e colunas
print(data.iloc[:, :])
print(data.iloc[0,1])
print(data.iloc[:,0])

# - forma 3: Pelos indices das linhas e nome das colunas
# neste caso usamos a funcao loc (q localiza as linhas pelo imdex e as colunas pelo nome)
#dados [linhas, colunas]
print(data.loc[0:10, 'price'])
print(data.loc[0:10, ['price','id','date']])
#ou 

cols = ['price','id','date']
print(data.loc[0:10, cols])


# - forma 4: Pelos indices booleanos
# 1 = true e 0 = false

cols = [True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
print(data.loc[0:10,cols])

# 5  Executando e respondendo o processo planejado e as perguntas de negocio:
import pandas as pd
data = pd.read_csv('kc_house_data.csv')

# qual a data do imovel mais antigo no portfolio? 
# R: ordenar o conjunto de dados pela menor data
data['date'] = pd.to_datetime(data['date'])
print(data.sort_values('date',ascending=True))


# quantos imoveis possuem o numero maximo de andares?
# R: encontar o numero de andars e determinar o maior
#    contar quantos imoveis eu tenho por andar

print(data['floors'].unique())

print(data[data['floors']==3.5].shape)
print(data.loc[data['floors']==3.5].shape)


# criar uma classificacao para imoveis, separando-os em baixo e alto padrao, de acordo com o preco. acima de 540.000 -> alto padrao (high_standard)
#                                                                                                  abaixo de 540.000 -> baixo padrao (low_standard)

# R: criar uma nova coluna no dataset e chamar de standard
#    para cada linha, comparar a coluna price
#    se price for maior que 540.000, escrever high_standard na coluna standard
#    se price for menor que 540.000, escrever low_standard na coluna standard
data['level'] = 'standard'
data.loc[data['price']>540000, 'level'] = 'high_level'

print(data.head())


# primeiro seleciona a coluna price
data['price'] 
#depois verifica todas as linha q sao maiores q 540000
data['price']  > 540000 # isso retorna um booleano q e o true e false
# com os booleanos na mao e possivel selecionar as linhas q sao true
data[data['price'] > 540000]
# agora seleciona-se as linhas de price acima de 540000 relacionadas com as linhas da coluna level, para isso deve-se colocar a funcao .loc
data.loc[data['price'] > 540000, 'level']
# agora substitui todas essas linhas standard da coluna level por high level
data.loc[data['price']>540000, 'level'] = 'high_level'


data.loc[data['price']<540000, 'level'] = 'low_level'
print(data.head())


# gostaria de um relatorio ordenado pelo preco e contendo as seguintes informacoes: 
# (id do imovel, 
# data q o imovel ficou disponivel para compra,
# o numeor de quartos,
# o tamanho total do terreno,
# o preco,
# a classificacao do imovel (alto e baixo))

# R: selecionar as colunas desejadas/demandadas
#    deletar as colunas desejadas/demandadas                                                                                               

report = data[['id','date','price','bedrooms','sqft_lot','level']].sort_values('price', ascending=False)
print(report)

#salvando arquivo em csv
report.to_csv('report_aula02.csv', index = False)

# gostaria de um mapa indicando onde as casas estao localizadas geograficamente 
                                                                                                  
# R:  procurar uma biblioteca em python q amrmazena uma funcao que desenha mapa.
#     aprender a user a funcao q desenha mapas    


# biblioteca plotly - armazena funcao q desenha mapa
# funcao scatter mapbox - funcao q desenha mapa

import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat = 'lat', lon = 'long', hover_name = 'id', hover_data = ['price'], 
                  color_discrete_sequence = 'fuchsia', zoom = 3, height = 300)

mapa.update_layout(mapbox_style = 'open-street-map')
mapa.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
mapa.show()


mapa.write_html('mapa_house.html')

# proximos exercicios

# 1 crie uma nova coluna chamada: "house_age"
# - se o valor da coluna "date" for maior que 2014-01-01 -> 'new_house'
# - se o valor da coluna "date" for menor que 2014-01-01 -> 'old_house'
import pandas as pd
data = pd.read_csv('kc_house_data.csv')
print(data.dtypes)

data['date'] = pd.to_datetime(data['date'])
print(data.dtypes)

data['house_age'] = 'house'

data['date'] > '2014-01-01 00:00:00'
data.loc[data['date'] > '2014-01-01 00:00:00', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01 00:00:00', 'house_age'] = 'old_house'

# 2 crie uma nova coluna chamada: "dormitory_type"
# - se o valor da coluna "bedrooms" for igual a 1 -> 'studio' 
# - se o valor da coluna "bedrooms" for igual a 2 -> 'apartament' 
# - se o valor da coluna "bedrooms" for maior q 2 -> 'house'

data['dormitory_type'] = 'd_type'
data.loc[data['bedrooms'].isin([0,1]), 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment' 
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

# 3 crie uma nova coluna chamada: "condition_type"
# - se o valor da coluna "condition" for menor ou igual a 2 -> 'bad'
# - se o valor da coluna "condition" for  igual a 3 ou 4 -> 'regular'
# - se o valor da coluna "condition" for igual a 5 -> 'good'

data['condition_type'] = 'c_type'
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'].isin([3,4]), 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'

# 4 modifique o TIPO a Coluna "condition" para STRING
data['condition'] = data['condition'].astype(str)
print(data.dtypes)

# 5 Delete as colunas: "sqft_living15"  e "sqft_lot15"
data = data.drop(['sqft_living15','sqft_lot15'], axis = 1)

# 6 Modifique o TIPO a Coluna "yr_build" para DATE
data['yr_built'] = pd.to_datetime(data['yr_built'],format= '%Y')
print(data.dtypes)
#
# 7 Modifique o TIPO a Coluna "yr_renovated" para DATE
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'], format = '%Y', errors = 'coerce')
print(data.dtypes)

# 8 Qual a data mais antiga de construcao de um  imovel?
print(data[['yr_built']].sort_values('yr_built', ascending=True))
#R : 1900

# 9 qual a data mais antiga de renovacao de um imovel?
print(data[['yr_renovated']].sort_values('yr_renovated', ascending=True))
#R: 1934

# 10 Qunatos imoveis tem 2 andares?
print(data[['id', 'floors']][data['floors']==2])


print(data['floors'].unique())

print(data[data['floors']==2].shape)
#R: 8241

# 11 Quantos imoveis estao com a condicao igual a "regular"?
print(data[['id', 'condition_type']][data['condition_type']=='regular'].shape)

print(data[data['condition_type']=='regular'].shape)
#R: 19710
 
# 12 Quantos imoveis estao com a condicao igual a "bad" e possuem "vista para o mar"?
print(data[(data['waterfront']==1) & (data['condition_type']=='bad')].shape)
#R: 2

# 13 Qunatos imoveis estao com a condicao igual a "good" e sao "new_house"?
print(data[(data['condition_type']=='good') & (data['house_age']=='new_house')].shape)
#R: 1701

# 14 Qual o valor do imovel mais caro do tipo "studio"?
print(data[['id','price','dormitory_type']][data['dormitory_type']=='studio'].sort_values('price', ascending=False))
#R: 1295650.0 

# 15 quantos imoveis do tipo "apartment" foram reformados em 2015?
print(data[(data['dormitory_type']=='apartment') & (data['yr_renovated'] == '2015-01-01 00:00:00')].shape)
#R:0

# 16 Qual o maoir numero de quartos que um imovel do tipo "house" possui?
print(data.loc[data['dormitory_type']== 'house','bedrooms'].max())
#R: 33
#ou
print(data[['bedrooms']][data['dormitory_type']== 'house'].sort_values('bedrooms', ascending=False))
#R:33

# 17  Quantos imoveis "new_house" foram reformados no ano de 2014?
print(data[(data['house_age']=='new_house') & (data['yr_renovated']=='2014-01-01 00:00:00')].shape)
#R:91


# 18 Selecione as colunas : "id", "date", "price", "floors", "zipcode" pelo metodo:

# 18.1 direto pelo nome das colunas
print(data[['id','date','price','floors','zipcode']])

# 18.2 pelo indices
print(data.iloc[:,[0,1,2,7,16]])
# 18.3 pelos indices das linhas e o nome das colunas
print(data.loc[:,['id','date','price','floors','zipcode']])
# 18.4  indices booleanos
cols = [True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False]
print(data.loc[:,cols])


#Obs: como saber o indece da coluna
data.columns.get_loc("zipcode")


# 19 Salve um arquivo .csv com somente as colunas do intem 10 ao 17
new_data=data.iloc[:,10:18]
print(new_data)
new_data.to_csv('new_data_q19.csv', index = False)


# 20 Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"

#nao fiz pq deu erro no primeiro



