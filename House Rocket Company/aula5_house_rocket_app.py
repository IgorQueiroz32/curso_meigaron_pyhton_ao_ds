#aula 5 parte 2
# Instalando o streamlit
# temq usar o terminal do pycharm
# este pacote e utilizado em python para criar apps
# para instalar, digite no terminal: pip install streamlit -> streamlit hello ->streamlit run aula5_house_rocket_app.py
#CTRL + S para sempre recarregar os codigos do pycharm no site do streamlit
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
st.title('House Rocket Company')

st.markdown('Welcome to House Rocket Data Analysis')
st.header('Load data')

# read data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])

    return data

# Load data
data = get_data('C:/spyder python/curso meigaron python ds/projetos portifolio/insight/House Rocket Company/kc_house_data.csv')
st.dataframe(data.head())

#  #Filter bedrooms
# f_attributes = st.sidebar.multiselect('Enter columns', data.columns) # 2.3.2
# f_bedrooms = st.sidebar.multiselect('Enter bedrooms ',
#                                    data['bedrooms'].sort_values().unique()) # 2.3.1
#
# st.title('Data Overview')
#
# # attributes + zipcode = select columns and rows
# # attributes = select columns
# # zipcode = select  rows
# # 0 + 0 = return original dataset
#
# if (f_bedrooms !=[]) & (f_attributes !=[]):
#     data = data.loc[data['bedrooms'].isin(f_bedrooms), f_attributes]
#
# elif (f_bedrooms !=[]) & (f_attributes ==[]):
#     data = data.loc[data['bedrooms'].isin(f_bedrooms), :]
#
# elif (f_bedrooms == []) & (f_attributes != []):
#     data = data.loc[:, f_attributes]
#
# else:
#     data = data.copy()
#
# st.dataframe(data) # funcao write escreve a tabela no site

#Filter bedrooms
f_bedrooms = st.sidebar.multiselect('Enter bedrooms ',
                                   data['bedrooms'].sort_values().unique()) # 2.3.1

st.title('Data Overview')

# attributes + zipcode = select columns and rows
# attributes = select columns
# zipcode = select  rows
# 0 + 0 = return original dataset

if f_bedrooms !=[]:
    data = data.loc[data['bedrooms'].isin(f_bedrooms)]

else:
    data = data.copy()

st.dataframe(data) # funcao write escreve a tabela no site


#plot map
st.title('House Rocket Map')
is_check = st.checkbox('Display Map')

#filters map
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())

price_slider = st.slider('Price Range',
                         price_min,
                         price_max,
                         price_avg)

if is_check:
    #select rows
    houses = data[data['price'] <= price_slider][['id','lat','long','price']]

    st.dataframe(houses)

    #draw map

    fig = px.scatter_mapbox(houses, lat='lat', lon='long', size='price',
                             color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    st.plotly_chart(fig)