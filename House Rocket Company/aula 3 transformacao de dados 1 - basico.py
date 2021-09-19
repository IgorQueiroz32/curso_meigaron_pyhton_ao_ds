# agenda:
#1. novas perguntas de negocio
#2. planejamento da solucao
#3. estrutura de dados
#4. transformacao de dados
#5. exervivios praticos.

#1. novas perguntas de negocio
# 1.1 recapitulando o desafio
#- empresa: house rocket
#- modelo de negocio: compra e venda de imoveis(lucro=venda - compra)
#- qual desafio: encontrar bons negocios. encontrar casas com preco baixo e com um alto potencial de revenda por um preco mais alto.

#1.2 novas perguntas do ceo pra vc:
#1.2.1 qual o numero de imoveis por ano de construcao?
#1.2.2 qual o menor numero de quartos por ano de construcao de imoveis?
#1.2.3 qual o preco de compra mais alto por cada numero de quarto?
#1.2.4 qual a soma de todos os precos de compra por numero de quartos?
#1.2.5 qual a soma de todos os precos de compra por numero de quartos e banheiros?
#1.2.6 qual o tamanho medio das salas dos imoveis por ano de construcao?
#1.2.7 qual o tamanho mediano das salas dos imoveis por ano de construcao?
#1.2.8 qual o desvio-padrao do tamanho das salas dos imoveis por ano de construcao?
#1.2.9 como e o crescimento medio de precos de compras dos imoveis, por ano, por dia e pela semana do ano?
#1.2.10 eu gostaria de olhar no mapa e conseguir identificar as casas com o maior preco.

#2. planejamento da solucao

#2.1 produto final ( o q entregar? planilha, grafico, modelo ML) 
#R: email (pergunta e resposta) + 2 anexos (anexo 1 : um dashboard com 3 graficos, anexo 2: um mapa no formato html)

#2.2 ferramenta (qual ferramenta usar?)
#R: python and jupyter notebook

#2.3 processo (como fazer?)
#R: 

#1.2.1 qual o numero de imoveis por ano de construcao?
#- conatr o numero de ids por ano de construcao

#1.2.2 qual o menor numero de quartos por ano de construcao de imoveis?
# - filtar os imoveis por ano de construcao e selecionar o menor numero de quartos

#1.2.3 qual o preco de compra mais alto por cada numero de quarto?
# - filtar os imoveis por numero de quartos e selecionar o de maior valor

#1.2.4 qual a soma de todos os precos de compra por numero de quartos?
# - filtar os imoveis por numero de quartos e somar todos os precos

#1.2.5 qual a soma de todos os precos de compra por numero de quartos e banheiros?
# - filtar os imoveis por numero de quartos e banheiros e realiza a  soma de  todos os precos

#1.2.6 qual o tamanho medio das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer media do tamanho das salas

#1.2.7 qual o tamanho mediano das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer a mediana do tamanho das salas

#1.2.8 qual o desvio-padrao do tamanho das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer o desvio-padrao do tamanho das salas

#1.2.9 como e o crescimento medio de precos de compras dos imoveis, por ano, por dia e pela semana do ano?
# - filtar os imoveis por ano e fazer um grafico onde o eixo x tem o ano e o eixo y tem a media do preco daquele ano
# - estudar uma biblioteca com funcao de grafico de linhas

#1.2.10 eu gostaria de olhar no mapa e conseguir identificar as casas com o maior preco.
# - modificar o mapa da aula anterior fazendo com q os pontos tenham o tamanho dependente do preco.


# 3 ferramentas para criar codigos em python:
#- IDEs
#       -pycharm
#       -vscode
#       -spyder
#       jupyterlab

#-notebooks
#       -jupyter notebook
#       -jupyter notebook vantagem e desvatagem: IDE e sempre necessario executar todos os camndos para codigo de maquina, todas as vezes q vc quiser executar seu script.
#       - no notebook e possivel rodar comandos independentemente um dos outros
#       - organizar melhor seus codigos
#       - a analise exploratoria de dados fica mais facil e mais organizada
#       - storytelling

# instalar o anaconda


# 4 EStrutura de daos em python

# - As 4 estruturas de daos mais usadas em python sao:
#       - listas (aula 4)
#       - dicionarios
#       - Tuples(aula 4)
#       - dataframes 


#4.1 dicionarios: 
#       - estrutura de dados que armazena informacao em uma estrutura de chave-valor
#       - todod os dados armazenados no dicionario precisam ter uma chave
#       - precisam de um nome
#       - nao aceita valores dupicados (mesmo par chave-valor)

# estrutura de dados - dicionario
d={'chave01':valor01,'chave02':valor02,'chave03':valor03,'chave04':valor04}

skirt={'size':'M', 'price': 139.90, 'color':'black'}
skirt={'size':'M', 'price': 139.90, 'color':'black', 'date': '2020-01-01'}
skirt={'size':'M', 'price': 139.90, 'color':['black','red','blue'],'date': '2020-01-01'}

# acessar os valores do dicionario
skirt['size']-> 'M'
skirt['color'] ->['black','red','blue']
skirt['color'][0] ->'black'

# como criar um dicionario vazio
skirt={}

#adiciono novos dados dentro de um dicionario
skirt['category']='bottom'

#nao aceita valores duplicados


#4.2 dataframes: 
#       - armazenam dados na forma tabular com nomes nas linhas e colunas
#       - precisam de um nome

# como criar um dataframe vazio
data = pd.DataFrame()

# como popular um dataframe vazio:
## atraves de um dicionario
import pandas as pd
data = {'size':['P','M','G'], 'price':[139.90, 59.90, 29.90], 'color':['black','red','blue']}

data=pd.DataFrame(data)

#5 Transformacao de Dados

# - Agrupamento
# - Operacoes matematicas

#5.1 Agrupameno:
    #-Sequencia de 3 tarefas: Split; Apply; Combine (Separa, Aplica e Combina)
    
#5.2 Operacoes:
    #- Com os dados agrupados, podemos realizar operacoes matematicas:
        #-Exemplos:
            #- contagem
            #- minimos
            #- maximos
            #- soma
            #- media
            #- mediana
            #- Desvio padrao
            
#6- Executando o processo planejado:
    
#6.1 qual o numero de imoveis por ano de construcao?
#- conatr o numero de ids por ano de construcao

#6.2 qual o menor numero de quartos por ano de construcao de imoveis?
# - filtar os imoveis por ano de construcao e selecionar o menor numero de quartos

#6.3 qual o preco de compra mais alto por cada numero de quarto?
# - filtar os imoveis por numero de quartos e selecionar o de maior valor

#6.4 qual a soma de todos os precos de compra por numero de quartos?
# - filtar os imoveis por numero de quartos e somar todos os precos

#6.5 qual a soma de todos os precos de compra por numero de quartos e banheiros?
# - filtar os imoveis por numero de quartos e banheiros e realiza a  soma de  todos os precos

#6.6 qual o tamanho medio das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer media do tamanho das salas

#6.7 qual o tamanho mediano das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer a mediana do tamanho das salas

#6.8 qual o desvio-padrao do tamanho das salas dos imoveis por ano de construcao?
# - filtar os imoveis por ano de construcao e fazer o desvio-padrao do tamanho das salas

#6.9 como e o crescimento medio de precos de compras dos imoveis, por ano, por dia e pela semana do ano?
# - filtar os imoveis por ano e fazer um grafico onde o eixo x tem o ano e o eixo y tem a media do preco daquele ano
# - estudar uma biblioteca com funcao de grafico de linhas

#6.10 eu gostaria de olhar no mapa e conseguir identificar as casas com o maior preco.
# - modificar o mapa da aula anterior fazendo com q os pontos tenham o tamanho dependente do preco.    

#7- nNovas perguntas do CEO:
    
#7.1 Crie uma nova coluna chamada: 'dormitory_type'
    #- Se o valor da coluna "bedrooms" for igual a 1 -> 'studio'
    #- Se o valor da coluna "bedrooms" for igual a 2 -> 'apartment'
    #- Se o valor da coluna "bedrooms" for maior q 2 -> 'house'

#7.2 FAca um grafico de barras que represente a soma dos precos pelo numero de quartos.

#7.3 FAca um grafico de linhas que represente a media dos precos pelo ano de construcao dos imoveis.

#7.4 FAca um grafico de barras que represente a media dos precos pelo tipo dos dormitorios.

#7.5 FAca um grafico de linha que mostre a evolucao da media dos precos pelo ano da reforma dos imoveis,
    # ap partir do ano de 1930.

#7.6 FAca uma tabela que mostre a media dos precos por ano de construcao e tipo de dormitorio dos imoveis,

#7.7 Crie um dashboard com os graficos das questoes 02, 03 e 04 (Dashboard: 1 linha e 2 colunas)

#7.8 Crie um dashboard com os graficos das questoes 02 e 04 (Dashboard: 2 colunas)

#7.9 Crie um dashboard com os graficos das questoes  03 e 05 (Dashboard: 2 linha)

#7.10 Faca um grafico com o tamanho dos pontos sendo igual ao tamanho da sala de estar.
            



