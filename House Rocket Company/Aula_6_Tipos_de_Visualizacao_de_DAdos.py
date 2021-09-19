import    pandas as pd
import streamlit as st
import     numpy as np
import    plotly.express as px
import    folium
import geopandas
from streamlit_folium import folium_static
from folium.plugins   import MarkerCluster
from datetime         import datetime


st.set_page_config(layout='wide')# deixa a tabela no site maior, mais larga

# read data
@st.cache(allow_output_mutation=True) # funcao q permite ler os dados da memoria virtual
def get_data(path):
    data = pd.read_csv(path)

    return data

def get_geofile(url):
    geofile = geopandas.read_file(url) # geopandas le arquivos geofiles

    return geofile

# Load data
path = 'C:/spyder python/curso meigaron python ds/projetos portifolio/insight/House Rocket Company/kc_house_data.csv'
data = get_data(path)

#Get geofile
url = 'http://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
geofile = get_geofile(url)
#add new features

#add new features

# preco por metro quadrado
data['m2_lot'] = data['sqft_lot'] * 0.0929
data['price_m2'] = data['price']/data['m2_lot']

#===========================================
# Data Overview
#============================================

f_attributes = st.sidebar.multiselect('Enter columns', data.columns) #  questao 3.3.2
f_zipcode = st.sidebar.multiselect('Enter zipcode',
                                   data['zipcode'].sort_values().unique()) # 3.3.1

st.title('Data Overview')

# attributes + zipcode = select columns and rows
# attributes = select columns
# zipcode = select  rows
# 0 + 0 = return original dataset

# juntando os filtros e anexando ao dataset
if (f_zipcode !=[]) & (f_attributes !=[]):
    data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
    # anexando as linhas do zipcode dentro do botao f_zipcode, e anexando as colunas dentro do f_attributes

elif (f_zipcode !=[]) & (f_attributes ==[]):
    data = data.loc[data['zipcode'].isin(f_zipcode), :]

elif (f_zipcode == []) & (f_attributes != []):
    data = data.loc[:, f_attributes]

else:
    data = data.copy()

st.dataframe(data) # funcao write escreve a tabela no site
#questoes um e dois feitas


#questao 3 abaixo
c1,c2 = st.beta_columns((1,1)) # serve para colocar tabelas uma do lado da outra
#Average metrics

df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

#Merge = so faz pares de 2 a 2
m1 = pd.merge(df1,df2, on='zipcode', how='inner')
m2 = pd.merge(m1,df3, on='zipcode', how='inner')
df = pd.merge(m2,df4, on='zipcode', how='inner')

df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQFT LIVING', 'PRICE/M2']

c1.header('Average Values')
c1.dataframe(df, height=600)

#questao 3 feita

#questao 4

# Descriptive Statistic
num_attributes = data.select_dtypes(include=['int64', 'float64'])# seleciona as colunas pelo tipo, neste caso, numericas

# central tendency - media, mediana
media =   pd.DataFrame (num_attributes.apply(np.mean, axis=0)) # funcao apply aplica qualquer funcao nas colunas ou linhas da variaves
mediana = pd.DataFrame (num_attributes.apply(np.median, axis=0))

# dispersion - std, min, max
std =  pd.DataFrame (num_attributes.apply(np.std, axis=0))
min_ = pd.DataFrame (num_attributes.apply(np.min, axis=0))
max_ = pd.DataFrame (num_attributes.apply(np.max, axis=0))

df5 = pd.concat([max_,min_,media,mediana,std],axis=1).reset_index()
df5.columns = ['attributes', 'max','min','mean','median','std']
pd.set_option('display.float_format', lambda x: '%.3f' % x)
c2.header('Descriptive Statistic')
c2.dataframe(df5, height=800)

# diferenca entre merge e concat:

# merge garante q os valores das colunas do df1 seja igual aos
#valores das colunas do df2.

# o concat nao garante isso, se a ordem dos dataframes estiverem diferentes ele concatena
# assim mesmo, nao oroganizando os valores dos dataframes assim como o merge faz.

# questao 4 feita

#===========================================
#  Portfolio Density
#============================================

# questao 5

st.title('Region Overview')
c1,c2 = st.beta_columns((1,1))
c1.header('Portfolio Density')

df = data

# Base MAp - Folium library mapa vazio
# densidade de casas por regiao
# este mapa verifica a quantidade e localizacao das casas por regiao
# pra este mapa usa-se o folium, o foilum static e o MarkerCluster
density_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                        default_zoom_start=15)

marker_cluster = MarkerCluster().add_to(density_map)
for name, row in df.iterrows():
    folium.Marker([row['lat'],row['long']],
                  popup= 'Sold ${0} on {1}. Features: {2} sqft,'
                         ' {3} bedrooms, {4} bathrooms,'
                         ' year build: {5}'. format(row['price'],
                                                    row['date'],
                                                    row['sqft_living'],
                                                    row['bedrooms'],
                                                    row['bathrooms'],
                                                    row['yr_built'])).add_to(marker_cluster)

with c1:
    folium_static(density_map)

# Region Price Map
# media de preco por regiao
# este mapa colore as regioes por media de preco, mais escura a cor maior a media de preco
# pra este mapa usa-se o geopandas, o folium, o foilum static e o MarkerCluster
c2.header('Price Density')

df = data[['price', 'zipcode' ]].groupby('zipcode').mean().reset_index()
df.columns = ['ZIP', 'PRICE']

# geofile ( arquivos espaciais (jsons-dicionarios - listas de coordenadas e zipcodes)
# de coordenadas geograficas de regioes, que formam formas geometricas)
# aki usa-se o geofile da regiao de seatle
# este arquivo e obtido em 'http://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())] # filtrando o geofile somente
# com os zips existentes no dataset
# os zips do geofile tem q estar dentro dos zips do dataset, usando somente as regioes existentes no dataset


region_price_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                        default_zoom_start=15)

folium.features.Choropleth(data=df,
                           geo_data=geofile,
                           columns=['ZIP', 'PRICE'],
                           key_on='feature.properties.ZIP',  # key_on junta o zip dos dois datasets
                           fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='AVG PRICE').add_to(region_price_map)

with c2:
    folium_static(region_price_map)

# questao 5 feita

# questao 6 e 7
#======================================
# Distribuicao dos imoveis por categorias comerciais
#================================================
st.sidebar.title('Comercial Options')
st.title('Comercial Attributes')

#--------------- Average price per year
st.header('Average Price per Year Built')
st.sidebar.subheader('Select Max Year Built')

#filters
min_year_built = int(data['yr_built'].min())
max_year_built = int(data['yr_built'].max())

f_year_built = st.sidebar.slider('Year Built', min_year_built,
                                               max_year_built,
                                               min_year_built)

#data selection
df = data.loc[data['yr_built'] <= f_year_built]

#data filtering
by_year = df[['price', 'yr_built']].groupby('yr_built').mean().reset_index()

#plot
fig = px.line(by_year, x='yr_built', y='price')
st.plotly_chart(fig, use_container_width=True)

#--------------- Average price per Day
st.header('Average Price per Day')
st.sidebar.subheader('Select Max Date')

#changind date type
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y%m%d')

#filters
min_date = datetime.strptime(data['date'].min(), '%Y%m%d')
max_date = datetime.strptime(data['date'].max(), '%Y%m%d')

f_date = st.sidebar.slider('Date', min_date,
                                   max_date,
                                   min_date)

#data selection
data['date'] = pd.to_datetime(data['date'])
df = data.loc[data['date'] <= f_date]

#data filtering
by_day = df[['price', 'date']].groupby('date').mean().reset_index()

#plot
fig = px.line(by_day, x='date', y='price')
st.plotly_chart(fig, use_container_width=True)

# questao 6 e 7 feitas

# questao 8

#==================================
# Distribuicao dos imoveis por preco
#===========================================
# faz -se uma distribuicao de preco dos imoveis por quantidade de imoveis

#-------------Histograma
# ----------------------------Price
st.header('Price Distribution')
st.sidebar.subheader('Select Max Price')

#filters
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())

f_price = st.sidebar.slider('Price',
                         price_min,
                         price_max,
                         price_avg)

#data selection
df = data.loc[data['price'] <= f_price]

#plot
fig = px.histogram(df, x='price', nbins=50)
st.plotly_chart(fig, use_container_width=True)

#==================================
# Distribuicao dos imoveis por categorias fisicas
#===========================================
st.sidebar.title('Atributes Options')
st.title('House Attributes')

#filters
f_bedrooms = st.sidebar.selectbox('Max of bedrooms',
                                  data['bedrooms'].sort_values().unique())

f_bathrooms = st.sidebar.selectbox('Max of bathrooms',
                                   data['bathrooms'].sort_values().unique())

c1,c2 = st.beta_columns(2)

# data selection and Plot House per bedrooms
c1.header('House per bedrooms')
df = data.loc[data['bedrooms'] < f_bedrooms]
fig = px.histogram(df, x='bedrooms', nbins=19)
c1.plotly_chart(fig, use_container_width=True)

# data selection and Plot House per bathrooms
c2.header('House per bathrooms')
df = data.loc[data['bathrooms'] < f_bathrooms]
fig = px.histogram(df, x='bathrooms', nbins=19)
c2.plotly_chart(fig, use_container_width=True)

f_floors = st.sidebar.selectbox('Max Number of floors',
                                data['floors'].sort_values().unique())

f_water_view = st.sidebar.checkbox('Only Houses with Water View')

c1, c2 = st.beta_columns(2)

# data selection and Plot House per floors
c1.header('House per floors')
df = data.loc[data['floors'] < f_floors]
fig = px.histogram(df, x='floors', nbins=19)
c1.plotly_chart(fig, use_container_width=True)

# data selection and Plot House per water view
c2.header('House per water view')

if f_water_view:# se clicar no botao aparece as casas de frente para o mar,
                #desclicando aparece todos os dados
    df = data[data['waterfront'] == 1]

else:
    df = data.copy()

fig = px.histogram(df, x='waterfront', nbins=10)
c2.plotly_chart(fig, use_container_width=True)

#### VISITAR SITE AWESOEM - STREAMLIT, TEM VARIOS EXEMPLOS DE DASHBOARD LEGAIS
