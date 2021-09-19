
# ----------------------------------------
# Libraries
# ---------------------------------------

import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import ipywidgets as widgets
from ipywidgets import fixed
from matplotlib import gridspec
from matplotlib import pyplot as plt
import plotly.express as px
import ipywidgets as ipywidgets
from ipywidgets import Box
import streamlit as st

st.markdown('House Rocket Data Analysis Exercises 5')
st.header('Load data')

# read data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
    return data

# Load data
data = get_data('C:/spyder python/curso meigaron python ds/projetos portifolio/insight/House Rocket Company/kc_house_data.csv')

# Creating new variables
data['is_waterfront'] = data['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')

data['nivel'] = data['price'].apply(lambda x: 0 if (x >= 0)      & (x < 321950)  else
                                              1 if (x >= 321950) & (x < 450000)  else
                                              2 if (x >= 450000) & (x < 645000)  else
                                              3                                       )

data['size'] = data['sqft_living'].apply(lambda x: 0 if (x >= 0)    & (x < 1427) else
                                                   1 if (x >= 1427) & (x < 1910) else
                                                   2 if (x >= 1910) & (x < 2550) else
                                                   3                                   )

st.dataframe(data)


# #plot map
is_check4 = st.sidebar.checkbox('House Rocket Map')
if is_check4:
    st.title('House Rocket Map')
    #FILTERS MAP


    # price filter
    price_min = int(data['price'].min())
    price_max = int(data['price'].max())
    price_avg = int(data['price'].mean())

    price_slider = st.slider('Price Range',
                             price_min,
                             price_max,
                             price_avg)


    # #is_waterfront filter
    is_waterfront_bar_multiselect = st.multiselect('Waterfront View',
                                       data['is_waterfront'].unique()) # 2.3.1

    if is_waterfront_bar_multiselect !=[]:
        waterfront_bar = str(data.loc[data['is_waterfront'].isin(is_waterfront_bar_multiselect)])

    else:
        waterfront_bar = data['is_waterfront']



    # #select rows
    houses = data[(data['price'] <= price_slider),
                  waterfront_bar][['id', 'lat', 'long', 'price', 'is_waterfront']]

    st.dataframe(houses)

    # #draw map
    #
    # fig = px.scatter_mapbox(houses,
    #                     lat = 'lat',
    #                     lon = 'long',
    #                     color = 'condition',
    #                     size = 'price',
    #                     color_continuous_scale = px.colors.cyclical.IceFire,
    #                     size_max = 15,
    #                     zoom = 10)
    #
    # fig.update_layout(mapbox_style='open-street-map')
    # fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    # st.plotly_chart(fig)

    # NAO FUNCIONA