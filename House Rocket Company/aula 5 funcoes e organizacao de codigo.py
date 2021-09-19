# agenda:
#1. recapitulando
#2. novas perguntas de negocio
#3. planejamento da solucao
#4. Diferenca entre um codigo amador e um profissional
#5. O que sao funcoes e pq sao uteis
#6. Criar Dashboards interativos na Web
#7. Exercicios

#1. recapitulando
# Aula 1: comecando com o python
# Aula 2: extracao e manipulacao de dados
# Aula 3: transformacao de dados 
# Aula 4: estruturas de controle


# 1.1 recapitulando o desafio
#- empresa: house rocket
#- modelo de negocio: compra e venda de imoveis(lucro=venda - compra)
#- qual desafio: encontrar bons negocios. encontrar casas com preco baixo e com um alto potencial de revenda por um preco mais alto.

#2. novas perguntas de negocio

# 2.1 Nao conseguindo usar o mapa que vc me enviou por email.
    
# 2.2 preciso acessar o mapa e o dashboard do meu celular.
    
    
#3. planejamento da solucao    
    
#3.1 produto final ( o q entregar? planilha, grafico, modelo ML) 
#R: Um link (URL) https://www.houserocket.dashboard.com.br
        #- Informacoes importantes
        #- Mapa interativo
        #- Dashboard interativo

#3.2 ferramenta (qual ferramenta usar?)
#R: python and jupyter notebook and pycharm

#3.3 processo (como fazer?)
#R: Organizar meus codigos em funcoes.
    #- Pesquisar uma biblioteca com funcoes para criar mapas que podem ser acessados pelo browser.
    
#4. A diferenca de um codigo amador x profissional

#4.1 Profissional Junior x Prifissional Senior

        #4.1.1 Junior:
            #- Faz codigo macarronico ( todo linear)
            #- Faz codigo so pra ele, ninguem entende
            #- Nao usa as esrtruturas de dados corretamente, e acha q so existe dataframe
            #- Nao usa funcoes (diretamente relacionado ao codigo macarronico)
            #- Nao organiza codigo de forma logica e simples ( so existe na cabeca dele)
            
        #4.1.2 Senior:
            #- Faz codigo modular ( sequencia de modulos)
            #- Outras pessoas usam seus codigos, faz o codigo para seu time e empresa.
            #- Sabe exatamente quando usar as estruturas de dados
            #- Sabe usar funcoes, para modularizar e escalar seu codigo, com sabedoria
            #- Seus codigos parecem livros, faceis de serem lidos, interpretados, reutizados.
            
#5. Funcao - E uma sequencia de comandos, q se repete varias vezes no script,
            # inves de escrever tod hr um monte de comando, coloca-se tudo isso num funcao, escreve
            # uma vez so, e depois usa-se a funcao.
            
            #condicoes da funcao: so escreve ela se so tiver mais repeticao e utilizacao dela no codigo.
            
            #  Requisitos de uma funcao:
            #    1. NOme -  Em relacao a sua responsabilidade 
            #    2. INput - parametros de entrada
            #    1. output -  dados de saida

# exemplo de funcao
def show_dtypes(data): # so se pode usar dados previamente declarados dentro da funcao, como o data por exemplo
    print(data.dtypes) 
    return None


#PRODUTO DE DADOS E FORMADO POR 3 ELEMENTOS: SOLUCAO DE DADOS ESCALAVEL, COM CODIGO PROFISSIONAL E SEJA 
# MODULARIZADO
    
# 6. Exercicios:
    
#6.1 Organizar o codigo da aula 04 em funcoes.
#6.2 Refazer o grafico e o dashboard com Streamlit
#6.3 Testar novos tipos de filtros 