# agenda:
#1. recapitulando as requisicoes do CEO
#2. Repassando pelo planejamento do dashboard
#3. Finalizacao do Dashboard Web
#4. Publicacao do Dashboard no Heroku

#1. recapitulando as requisicoes do CEO

#1.1 Gostaria de chegar de manha na minha mesa e ter um lugar unico onde eu possa observar o portifolio da
# House Rocket. Nesse portifolio, eu tenho interesse:
    
    #1 - Filtros do imoveis por um ou varias regioes.
    #2 - Escolher uma ou mais variaveis para visualizar.
    #3 - Observar o numero total de imoveis a meida de preco, a media da sala de estar e tambem a media do preco
        #por metro quadrado em cada um dos codiogos postais.
    #4 - Analisar cada uma das colunas de um modo mais descrito.
    #5 - Um mapa com a densidade de portifolio por regiao e tambem densidade de preco.
    #6 - Checar a variacao anual de preco.
    #7 - Checar a variacao diaria de preco.
    #8 - Conferir a distribuicao dos imoveis por:
            #- preco;
            #- numero de quartos;
            #- numero de banheiros;
            #- numero de andares;
            #- vista pra agua ou nao.
    #9 - Ter autonomia para fazer as minhas proprias analises, atraves de filtros.
    
#3.1 produto final ( o q entregar? planilha, grafico, modelo ML) 
#R: Um link (URL) https://www.houserocket.dashboard.com.br para acessar o dashboard
        #- Informacoes importantes
        #- Mapa interativo
        #- Dashboard interativo

#3.2 ferramenta (qual ferramenta usar?)
#R: python and pycharm (IDE)

#3.3 processo (como fazer?)
    
    #1 - Filtros do imoveis por um ou varias regioes.
    
            #- Objetivo: Visualizar imoveis por codigo postal.
            #- Acao do Usuario: Digitar um ou mais codigos desejados.
            #- A visualizacao: Uma tabela com todos os atributos e filtrada por codigo postal.
    
    
    #2 - Escolher uma ou mais variaveis para visualizar.
    
            #- Objetivo: Visualizar as caracteristicas do imovel.
            #- Acao do Usuario: Digita as caracteristicas desejadas.
            #- A visualizacao: Uma tabela com todos os atributos selecionados.
            
            
    #3 - Observar o numero total de imoveis a meida de preco, a media da sala de estar e tambem a media do preco
        #por metro quadrado em cada um dos codiogos postais.
        
            #- Objetivo: Visualizar as medias de algumas metricas por regiao.
            #- Acao do Usuario: Digitar as metricas desejadas.
            #- A visualizacao: Uma tabela com todos os atributos selecionados.
        
        
    #4 - Analisar cada uma das colunas de um modo mais descritivo.
    
            #- Objetivo: Visualizar metricas descritivas de cada atributo escolhido.
            #- Acao do Usuario: Digitar as metricas desejadas.
            #- A visualizacao: Uma tabela com metricas descritivas por atributo.
            
            
    #5 - Um mapa com a densidade de portifolio por regiao e tambem densidade de preco.
    
            #- Objetivo: Visualizar a desnidade de portifolio no mapa (numero de imoveis por regiao) e 
                        # Visualizar a desnidade de preco
            #- Acao do Usuario: Nanhuema acao
            #- A visualizacao: Um mapa com a densidade de imoveis por regiao e por preco. 
            
            
    #6 - Checar a variacao anual de preco.
    
            #- Objetivo: Observar variacoes anuais de precos.
            #- Acao do Usuario: Filtra os dados por ano.
            #- A visualizacao: Um grafico de linha com oa anos em x e precos medios em y
            
            
    #7 - Checar a variacao diaria de preco.
    
            #- Objetivo: Observar variacoes diaris de precos.
            #- Acao do Usuario: Filtra os dados por dias.
            #- A visualizacao: Um grafico de linha com oa dias em x e precos medios em y
            
            
    #8 - Conferir a distribuicao dos imoveis por:
            #- preco;
            #- numero de quartos;
            #- numero de banheiros;
            #- numero de andares;
            #- vista pra agua ou nao.
            
                    #- Objetivo: Observar a concentracao dos imoveis por preco, quartos, banheiros,
                                # andares e vista pra agua.
                    #- Acao do Usuario: Filtro de preco, quartos, banheiros, andares e vista pra agua.
                    #- A visualizacao: Um histograma com cada atributo definido.
            
    
# Tabela -> Exploracao e Comparacao
# Linhas -> Crescimento ou decaimento
# Barras -> Comparar proporcoes
# Pizza -> Ate duas comparacoes
# Barras Empilhadas -> Comparar proporcoes percentualmente 