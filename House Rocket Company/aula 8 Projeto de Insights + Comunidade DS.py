# agenda:
#1. As etapas de um projeto de Ciencia de DAdos
#2. TRansformando o Python do zero ao DS em um projeto de Portifolio
#3. Tarefa pra casa
#4. Recapitulando o que foi aprendido ate agora.
#5. Comunidade DS

#1. As etapas de um projeto de Ciencia de DAdos

    #1.1 Questao de Negocio-> Entendimento do Negocio -> Coleta de DAdos -> 
    #-> Limpeza de dados -> Exploracao de dados -> Modelagem de Dados ->
    # -> Aplicacao dos algoritmos de ML -> Avaliacao da performance dos modelos ->
    # -> Publicacao do modelo (modelo em producao).

#2. O projeto do tipo Insights:
       
    # Objetivo: Gerar Insights atraves da analise e manipulacao dos dados para 
    # auxiliar a tomada de decisao pelo time de negocios.
    
    # Etapas: #2.1 Questao de Negocio-> Entendimento do Negocio -> Coleta de DAdos -> 
    #-> Limpeza de dados -> Exploracao de dados -> Publicacao do modelo (modelo em producao).

    # 2.0 Questao de Negocio
    
        # 1. Quais sao os imoveis que a House Rocket deveria comprar e por qul preco?
        # 2. Uma vez o imovel comprado, qual e o melhor momento para
        # vende-lo e por qual preco?
        
    # 2.1 Entendimento do Negocio
    
            # 2.1.1. Produto final (o que realmente eu vou entregar de concreto? Planilha, modelo ML, Email).
                # 2 Relatorios:
                    # - Relatorio com as sugestoes de compra de imovel por um valor recomendado.
                    # - Relatorio com as sugestoes de venda de um imovel por um valor recomendado.
            
            # 2.1.2 Qual sao as ferramentas (o que preciso para realizar esse projeto?)
                # - Python
                # - Pycharm
                # - Jupyter Notebook
        
            # 2.1.3. Processo (quais sao os pasos necessarios para alcancar meu objetivo?)
                    # 2.1.3.1. Quais sao os imoveis que a House Rocket deveria comprar e por qul preco?
                    
                        # - Plano 01: 
                            # - Coletar os dados do site do Kaggle.
                           
                            # - Agrupar os dados por regiao (zipcode) (agrupa-se por regiao pois
                                #e uma variavel q influencia muito o preco, nobres e nao tao nobres por exemplo)
                           
                            # - Dentro de cada regiao, eu vou encontrar a mediana do preco dos imoveis ( pois podem ter outliers)
                            
                            # - Vou sugerir que os imoveis que estao abaixo do preco mediano de cada
                                # regiao e que estejam em boas condicoes, sejam comprados
                    
                            # - Exemplo:
                                # - Imovel code | Regiao (zipcode) | preco do imovel | preco da mediana (preco de mercado daquela regiao) | condicao | Status
                                #-   10330      |   302349         | $ 450.000,00    | $ 500.000,00                                       | 3        | Compra
                                #-   10335      |   302349         | $ 750.000,00    | $ 500.000,00                                       | 3        | Nao Compra
                                #-   10345      |   302349         | $ 150.000,00    | $ 500.000,00                                       | 1        | Nao Compra
     
                                # - df['price_median] = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
                                
                                # - df2 = pd.merge(data, df, on = 'zipcode', how = 'inner')
                                
                               # for i in range(len(df2):
                                     #if (df2.loc[i,'price']<df2['price_median']) & (df2['condition']>= 3):
                                        # df2['status'] = 'compra'
                                         
                                     #else:
                                         #df2['status']
                                
                    # 2.1.3.2. Uma vez o imovel comprado, qual e o melhor momento para vende-lo e por qual preco?
                    
                        # - Plano 01: 
                            # - Com os dados ja tratados e organizados.
                            # - Agrupar os imoveis por regiao (zipcode) e por sazonalidade (Summer, Winter)
                            # - Dentro de cada regiao e sazonalidade, eu vou calcular a mediana de preco.
                            # - Condicoes de venda:
                                # 1. Se o preco da compra for maior que a mediana da regiao + a sazonalidade.
                                        # - O preco da venda sera igual ao preco da compra + 10 %
                                
                                 # 2. Se o preco da compra for menor que a mediana da regiao + a sazonalidade. 
                                        # - O preco da venda sera igual ao preco da compra + 30 %
                                        
                                        # - OBS: neste processo, apos todas as casas compradas (ou a comprar), cria-se uma  nova tabela,
                                            #- com a mediana da casas compradas por regiao, e apartir dessa mediana + a sazonalidade estipula-se 
                                            #- o valor de venda.
                                            
                             # - Exemplo:
                             # - Imovel code | Regiao (zipcode) | temporada| preco da compra | preco da mediana (preco de mercado daquela regiao) | preco da venda       | lucro
                             #-   10330      |   302349         | Verao    | $ 450.000,00    | $ 800.000,00                                       | $ 450.000,00  + 30%  |??
                             #-   10330      |   302349         | Inverno  | $ 450.000,00    | $ 400.000,00                                       | $ 450.000,00  + 30%  |??
        
        
    # 2.2 Coleta de DAdos    
    
        # - Coletar os dados do site do Kaggle (https:www.kaggle.com/harfoxem/housesaleprediction)
        
   
    # 2.3 Limpeza de Dados:
        
            # - Remover datas erradas;
            # - Remover outliers devido a erro do sistema
            
    
    # 2.4 Exploracao de dados (EDA)    
    
        # 2.4.1- Descobrir Insights para o time de negocio.
        # 2.4.2- Explorar os dados para identificar o impacto dos atributos nos algoritmos de ML.
       
        # 2.4.3- O que sao Insights para o negocio?
                # - Insights sao descoberts, atraves dos dados, que sao inesperadas pelas pessoas.    
                # - Insight precisa ser acionavel, ou seja, faz com a pessoa tome decisoes com isso. Caso contrario esse insight e somente uma curiosidade.
                    
                    # - Exemplos:
                                    #- Durante o periodo de natal, vende-se mais casas do que na pascoa (Descoberta)
                                    #- Imoveis com porao sao maiores do que imoveis sem porao (Nao acionavel)
                                    #- Imoveis com porao sao sao 40% mais caros do que os outros imoveis (Descoberta)
                                
        # 2.4.4- Como fazer para criar as hipoteses?
                # - Todas as hipoteses de negocio precisa ter 3 caracteristicas:
                    # - Precisa ser uma AFIRMACAO.
                    # - Precisa ser uma comparacao entre 2 variaveis.
                    # - Voce precisa definir um valor base.
                    
                    # - Exemplos de hipoteses para fazer como execicios:
                                    #- H1: Imoveis que possuem vista para agua, sao 20% mais caros, na media.
                                    #- H2: Imoveis com data de construcao menor que 1955, sao 50% mais baratos, na media.
                                    #- H3: Imoveis sem porao possuem area total (sqrt_lot), sao 40% maiores do que os imoveis com porao.
                                    #- H4: O crescimento do preco dos imoveis YoY (Year over Year) e de 10% ( preco medio de janeiro de um ano comparado ao preco medio de janeiro do outro ano)
                                    #- H5: Imoveis com 3 banheiros tem um crescimento de MoM ( Month over Month) de 15%
                                        
                                    #- As hipoteses podem ser apresentadas como tabelas, graficos, etc. E no final dela, e informado se e verdadeiro, 
                                        #se for falso, e informado o valor real.
                                        
                    # - Criar mais 5 hipoteses
        

#3. TRansformando o Python do zero ao DS em um projeto de Portifolio (Isso tudo vai no read me, la no github)
        
        
        #-3.1 O que e obrigatorio em um proeto de portifolio.
        
            #-3.1.1. Questao de negocio.
                #- O que voce quer resolver?
                   # Resposta:         # 1. Quais sao os imoveis que a House Rocket deveria comprar e por qul preco?
                                       # 2. Uma vez o imovel comprado, qual e o melhor momento para vende-lo e por qual preco?
                                       
                                
            #-3.1.2. Premissas do negocio.
                #- Tudo aquilo q vc assume pra resolver um problema.
                #- Vem de pesquisas previamente feitas sobre o negocio.
                #- A solucao deste problema e baseado em resultados fornecidos por essas premissas.
                    #- Exemplo:
                        #- A pesquisas informa q as casas fecham pra visita no inverno, devido as nevascas.
                        #- Assumir q valore acima de x sao outliers e sao excluidos por ser erros humanos.
                        

            #-3.1.3. Planejamento da solucao.
            
            #-3.1.4. Os 5 principais insights de negocio.
                #- sao insights acionaveis, sao descobertas q vieram da validacao de hipoteses, que tem uma afirmacao, um valor base line e uma comparacao entre duas variaveis do dataset
                
            #-3.1.4. Resultados financeiros ( quanto de dinheiro a empresa ganhara de dinheiro se implementar a solucao no dia a dia, melhorando a tomada de decisao)
                #- soma do lucro
                
            #-3.1.5. Conclusao
                #- Seu objetivo inicial foi alcancado?
                
            #-3.1.6. Proximos passos
                

#4. Tarefa para casa:      

        #-3.1 Criar visualizacoes para responder cada uma das 10 hipoteses de negocio.
        #-4.2 Construir uma tabela com as recomendacoes de compra ou nao compra.
        #-4.3 Construir uma tabela com recomendacoes de venda com acrescimo de 10 ou 30%.
        #-4.4 Fornecer as hipoteses e as tabelas no Streamlit.
        #-4.5 TRansformar o projeto do curso de Python do ZERO ao DS em um projeto de portfolio.
        #-4.6 Salvar os codigos dentro do GitHub
        #-4.7 Escrever o README com o srequisitos obrigatorios para um portfolio de projetos.
 
        
#5. Recapitulando o que foi aprendido ate agora.

    #-5.1 Aula 01: Comencando com python do zero
    #-5.2 Aula 02: Extracao e manipulacao de dados
    #-5.3 Aula 03: Transformacao de dados
    #-5.4 Aula 04: Estrutura de Dados
    #-5.5 Aula 05: Funcoes e organizacao de codigo
    #-5.6 Aula 06: Visualizacao de dados
    #-5.7 Aula 07: Visualizacao de dados 2
    #-5.8 Aula 08: Projeto de portifolio


#6. Proximos passos do curso em modulos: (curso de pyhton do DS ao DEV)
    
    #- Primeiro ciclo
        #- Modulo 01: Resolucao de exercicios do pyhton do zero ao ds
        #- Modulo 02: instalacao de ferramentas (linux, jupyter lab, git, github)
        #- Modulo 03: o novo problema de negocio
        #- Modulo 04: desenvolvimento do pensamento analitico
        #- Modulo 05: extracao de dado do HTML usando uma biblioteca chamada Beautiful Soup
        #- Modulo 06: extracao de dados do HTML de modo assincrono.
        #- Modulo 07: Banco de dados e SQL com Python
        #- Modulo 08: ambiente virtual em python
        #- Modulo 09: agendamento automatico de tarefas
        #- Modulo 10: primeira rodada de perguntas de negocios do CEO e analise
    
    #- Segundo ciclo
        #- Modulo 11: extracao de dados do HTML via Selenium
        #- Modulo 12: segundada rodada de perguntas de negocios do CEO e analise
        #- Modulo 13: Storytelling
        
    # Em torno de 50 aulas

    #- Formacao de python = curso de python do zero ao DS + 
    #-                        curso de pyhton do DS ao DEV
    
#7. Proximos caminhos a seguir: melhor seguir o curso DS em producao
                                 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        