# agenda:
#1. recapitulando
#2. novas perguntas de negocio
#3. planejamento da solucao
#4. estrutura de dados
#5. Estruturas de controle - condicionais
#6. Estruturas de controle - lacos

#1. recapitulando
# Aula 1: comecando com o python
# Aula 2: extracao e manipulacao de dados
# Aula 3: transformacao de dados 
# Aula 4: estruturas de controle

#-- proximo: 20% seguir estudando para analista de dados (python + SQL + storytelling + ETL + banco de dados)
#-- proximo: 30% seguir estudando para cientista de dados (machine learning + estatistica + Eng. software)

# 1.1 recapitulando o desafio
#- empresa: house rocket
#- modelo de negocio: compra e venda de imoveis(lucro=venda - compra)
#- qual desafio: encontrar bons negocios. encontrar casas com preco baixo e com um alto potencial de revenda por um preco mais alto.

#2. novas perguntas de negocio

# 2.1 Qual a quantidade de imoveis por nivel?
    #- NIvel 0: Preco entre R$ 0.00 e R$ 321.950
    #- NIvel 1: Preco entre R$ 321.950 e R$ 450.000
    #- NIvel 2: Preco entre R$ 450.000 e R$ 645.000
    #- NIvel 3: Preco acima de R$ 645.000
    
# 2.2 Adicione as seguintes informacoes ao imovel:
    #- NOme da rua
    #- Numero do imovel
    #- Nome do bairro
    #- Nome da cidade
    #- Nome do esado
    
# 2.3 Adicione o nivel do imovel no mapa como uma cor.

# 2.4 Adicione o preco do imovel como o tamanho do ponto no mapa.

# 2.5 Adicione opcoes de filtro para eu fazer minhas proprias analises.
    #- Eu quero escolher visualizar imoveis com vista para a agua ou nao.
    #- Eu quero escolher vfiltrar os imoveis ate um certo valor de preco.
 
# 2.5 Adicione opcoes de filtro no ultimo dashboard enviado.
    #- Eu quero visualizar somente valores a partir de uma data disponivel para compra.
    
#3. planejamento da solucao    
    
#3.1 produto final ( o q entregar? planilha, grafico, modelo ML) 
#R: email (pergunta e resposta) + 3 anexos (anexo 1: um arquivo .csv com as novas infomacoes requisitadas,
# anexo 2: um mapa com os filtros requisitados,
# anexo 3: um dashboard com os filtros requisitados)

#3.2 ferramenta (qual ferramenta usar?)
#R: python and jupyter notebook

#3.3 processo (como fazer?)
#R:   
    
# 3.1 Qual a quantidade de imoveis por nivel?
    #- NIvel 0: Preco entre R$ 0.00 e R$ 321.950
    #- NIvel 1: Preco entre R$ 321.950 e R$ 450.000
    #- NIvel 2: Preco entre R$ 450.000 e R$ 645.000
    #- NIvel 3: Preco acima de R$ 645.000
    
    # Popular uma nova coluna chamada Nivel com os valores condicionais aos intervalos
    
#3.2 Adicione as seguintes informacoes ao imovel:
    #- NOme da rua
    #- Numero do imovel
    #- Nome do bairro
    #- Nome da cidade
    #- Nome do esado
    
    # onde tem essas informacoes: tem no banco de dados da empresa? NAO
    # sao fornecidoas por uma API? SIM, API chamada GEOPY
    # Amigo com essas informacoes? NAO
    
    #qual dado eu tenho na minha base que eu consiga fazer o link? zipcode e lat/long
    # como coletar esse dado e como anexa-lo no conjunto de dados original.
    
# 3.3 Adicione o nivel do imovel no mapa como uma cor.

    #adicionar a coluna 'nivel' como uma cor do mapa.
    
# 3.4 Adicione o preco do imovel como o tamanho do ponto no mapa.

    #adicionar a coluna 'preco' como um tamanho no mapa.

# 3.5 Adicione opcoes de filtro para eu fazer minhas proprias analises.
    #- Eu quero escolher visualizar imoveis com vista para a agua ou nao.
    #- Eu quero escolher vfiltrar os imoveis ate um certo valor de preco.
    
        #encontrar uma biblioteca qye tenha funcoes que permitam colocar filtros no jupyter notebook. 
        # Entender o funcionamento da biblioteca e adicionar no jupyter notebook.
 
#3.6 Adicione opcoes de filtro no ultimo dashboard enviado.
    #- Eu quero visualizar somente valores a partir de uma data disponivel para compra.    
    
        #encontrar uma biblioteca qye tenha funcoes que permitam colocar filtros no jupyter notebook. 
        # Entender o funcionamento da biblioteca e adicionar no jupyter notebook.

    
#4. estrutura de dados em python    
    
    #-Listas
    #-Tuples (Aula avancada) (SQL + Python, muito usado em retorno de banco de dados)
    #- Dicionarios (Aula 3)
    #-Dataframes (Aula 3)
    
#4.1 Listas:
    #- POssui valores, tanto numericos quanto categoricos
    #- Os valores sao mapeados por posicao. ( cada dado e acessado pela sua posicao dentro de uma lista)
 
#5. Estruturas de controle - condicionais
    #-Condicional permite selecionar linhas ou colunas ate q a condicao seja satisfeita.
    #-Selecionar linhas e colunas combinando condicoes.
    
#6. Estruturas de controle - LAcos
    #-Lacos :
        #- Sao repeticoes de comandos ate q uma condicao seja satisfeita
        #-LAco FOR
            #-Aplica transformacoes de dados em inervalos excolhidos pelo time de negocio.
            #- E necessario conhecer o tamanho do laco (ate quando eu vou repetir os comandos)
        
        #- LAco WHILE
            #- Mantem o fluxo de codigo continuamente.
            #- Usado quando o tamanho do laco e desconhecido. 

# Exercicios            

# 7.1 Qual a media de preco de compra dos imoveis por Nivel?
    #- NIvel 0: Preco entre R$ 0.00 e R$ 321.950
    #- NIvel 1: Preco entre R$ 321.950 e R$ 450.000
    #- NIvel 2: Preco entre R$ 450.000 e R$ 645.000
    #- NIvel 3: Preco acima de R$ 645.000

# 7.2 Qual a media do tamanho da sala de estar dos imoveis por Size?
    #- Size 0: Tamanho entre 0 e 1427 sqft
    #- Size 1: Tamanho entre 1427 e 1910 sqft
    #- Size 2: Tamanho entre 1910 e 2550 sqft
    #- Size 3: Tamanho acima de 2550 sqft    

#7.3 Adicione as seguintes informacoes ao imovel:
    #- Place ID: Identificacao da localizacao
    #- OSM Type: Open Street Map type
    #- Country: Nome do pais
    #- Country Code: Codigo do pais
    
# 7.4 Adicione os seguintes filtros no mapa:
    #- 1Tamanho minimo da area de estar
    #- 2Valor maximo de preco    
    #- 3Tamanho maximo da area do porao  
    #- 4Filtro por ano de construcao    
    #- 5Numero minimo de banheiros
    #- 6Filtro da condicoes do imovel

#7.5 Adicione os seguintes filtros no dashboard:
    #- Filtro se possui vista pra agua ou nao
    #- Filtro por data disponivel da compra
    #- Filtro por ano de renovacao 

