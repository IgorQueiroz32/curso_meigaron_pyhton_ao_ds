
#house_rocket_exercicio2_aula5.py


# ----------------------------------------
# Libraries
# ---------------------------------------

import pandas as pd
import numpy as np
from matplotlib import gridspec
from matplotlib import pyplot as plt
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

st.title('House Rocket Company')

st.markdown('Welcome to House Rocket Data Analysis Exercise 5')
st.header('Select the checkboxes to visualise different data analyses')

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
#===========================================
# Data Overview
#============================================
is_check = st.sidebar.checkbox('Data Overview')
if is_check:
    f_attributes = st.sidebar.multiselect('Enter columns', data.columns)

    st.title('Data Overview')

    # attributes + zipcode = select columns and rows
    # attributes = select columns
    # zipcode = select  rows
    # 0 + 0 = return original dataset

    if f_attributes !=[]:
        data = data[f_attributes]

    else:
        data = data.copy()

    st.dataframe(data)

    #View Descriptive Statistic
    is_check1 = st.sidebar.checkbox('Descriptive Statistic House Rocket')
    if is_check1:
        # Descriptive Statistic
        num_attributes = data.select_dtypes(include=['int64', 'float64'])# seleciona as colunas pelo tipo, neste caso, numericas

            # central tendency - media, mediana
        media =   pd.DataFrame (num_attributes.apply(np.mean, axis=0)) # funcao apply aplica qualquer funcao nas colunas ou linhas da variaves
        mediana = pd.DataFrame (num_attributes.apply(np.median, axis=0))

        #    dispersion - std, min, max
        std =  pd.DataFrame (num_attributes.apply(np.std, axis=0))
        min_ = pd.DataFrame (num_attributes.apply(np.min, axis=0))
        max_ = pd.DataFrame (num_attributes.apply(np.max, axis=0))

        df1 = pd.concat([max_,min_,media,mediana,std],axis=1).reset_index()
        df1.columns = ['attributes', 'max','min','mean','median','std']
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        st.header('Descriptive Statistic House Rocket')
        st.dataframe(df1, height=800)

    # data type
    is_check2 = st.sidebar.checkbox('Data Type')
    if is_check2:
        st.title('Data Type')
        data.dtypes

    # data dimensions
    is_check3 = st.sidebar.checkbox('Data Dimensions')
    if is_check3:
        st.title('Data Dimensions')
        data_dimentions = str('Number of rows: {}'.format(data.shape[0])) + ' , ' + str(
            'Number of columns: {}'.format(data.shape[1]))
        st.write(data_dimentions)

# Average values
is_check4 = st.sidebar.checkbox('Average Values')
if is_check4:
    st.title('Average Values')
    c1, c2 = st.beta_columns((1, 1))

    df2 = data[['id', 'nivel']].groupby('nivel').count().reset_index()
    df3 = data[['price', 'nivel']].groupby('nivel').mean().reset_index()
    # Merge
    m1 = pd.merge(df2, df3, on='nivel', how='inner')

    m1.columns = ['NIVEL', 'TOTAL HOUSES', 'PRICE MEAN']

    c1.header('Average Values ID/PRICE')
    c1.dataframe(m1, height=600)

    df4 = data[['id', 'size']].groupby('size').count().reset_index()
    df5 = data[['sqft_living', 'size']].groupby('size').mean().reset_index()
    # Merge
    m2 = pd.merge(df4, df5, on='size', how='inner')

    m2.columns = ['SIZE', 'TOTAL HOUSES', 'SQFT LIVING MEAN']

    c2.header('Average Values ID/SQFT LIVING')
    c2.dataframe(m2, height=600)

#plot map
is_check5 = st.sidebar.checkbox('House Rocket Map')
if is_check5:
    st.title('House Rocket Map')
    #FILTERS MAP

    #sqft_living filter
    sqft_living_slider = st.select_slider('Living Room Size',
                             options=data['sqft_living'].sort_values().unique().tolist())

    # price filter
    price_min = int(data['price'].min())
    price_max = int(data['price'].max())
    price_avg = int(data['price'].mean())

    price_slider = st.slider('Price Range',
                             price_min,
                             price_max,
                             price_avg)

    #sqft_basement filter
    sqft_basement_slider = st.select_slider('Basement Room Size',
                             options=data['sqft_basement'].sort_values().unique().tolist())

    #yr_built filter
    yr_built_slider = st.select_slider('Year Built Range',
                             options=data['yr_built'].sort_values().unique().tolist())

    #yr_built filter
    bathrooms_slider = st.select_slider('Number of bathrooms',
                             options=data['bathrooms'].sort_values().unique().tolist())

    #yr_built filter
    condition_slider = st.select_slider('Houses Conditions',
                             options=data['condition'].sort_values().unique().tolist())

# # is_waterfront filter
# # is_waterfront_bar_multiselect = st.multiselect('Waterfront View',
# #                                    data['is_waterfront'].unique()) # 2.3.1
# #
# # if is_waterfront_bar_multiselect !=[]:
# #     data = data.loc[data['is_waterfront'].isin(is_waterfront_bar_multiselect)]
# #
# # else:
# #     data = data.copy()

    #select rows
    houses = data[(data['sqft_living'] <= sqft_living_slider) &
                  (data['price'] <= price_slider) &
                  (data['sqft_basement'] <= sqft_basement_slider) &
                  (data['yr_built'] == yr_built_slider) &
                  (data['bathrooms'] <= bathrooms_slider) &
                  (data['condition'] <= condition_slider) ][['id', 'lat', 'long', 'price',
                                                             'condition', 'bathrooms']]

    st.dataframe(houses)

    #draw map

    fig = px.scatter_mapbox(houses,
                        lat = 'lat',
                        lon = 'long',
                        color = 'condition',
                        size = 'price',
                        color_continuous_scale = px.colors.cyclical.IceFire,
                        size_max = 15,
                        zoom = 10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    st.plotly_chart(fig)

#plot dashboard
is_check6 = st.sidebar.checkbox('House Rocket Dashboard')
if is_check6:
    st.title('House Rocket Dashboard')

    # FILTERS DASHBOARD

    # yr_renovated filter
    yr_renovated_slider = st.select_slider('Year Renovated Range',
                             options=data['yr_renovated'].sort_values().unique().tolist())

    # buy date filter
    buy_date_slider = st.select_slider('Buy Date Range',
                             options=data['date'].sort_values().unique().tolist())

    # select rows
    df = data[(data['date'] == buy_date_slider) &
              (data['yr_renovated'] <= yr_renovated_slider)]

    st.dataframe(df)

    # creating dashboard
    fig = plt.figure(figsize=(21, 12))
    specs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

    ax1 = fig.add_subplot(specs[0, :])  # First row
    ax2 = fig.add_subplot(specs[1, 0])  # Second row, First column
    ax3 = fig.add_subplot(specs[1, 1])  # Second row, Second column

    # First graph
    by_year = df[['price', 'year']].groupby('year').sum().reset_index()
    ax1.bar(by_year['year'], by_year['price'])
    ax1.set_title('title: Avg Price by Year')

    # second graph
    by_day = df[['price', 'date']].groupby('date').mean().reset_index()
    ax2.plot(by_day['date'], by_day['price'])
    ax2.set_title('title: Avg Price by Day')
    plt.xticks(rotation=60);

    # third graph
    by_year_week = df[['price', 'year_week']].groupby('year_week').mean().reset_index()
    ax3.bar(by_year_week['year_week'], by_year_week['price'])
    ax3.set_title('title: Avg Price by Year - Week')
    plt.xticks(rotation=60);

# NAO FUNCIONOU:
# #### DASHBOARD NAO APARECE NO SITE
# NAO CONSEGUI COLOCAR NO MAPA E NO DASHBOARD INTERATIVO O BOTAO MULTISELECT
# NAO CONSEGUI CRIAR O GROUPBY INTERATIVO

# is_check7 = st.sidebar.checkbox('Interactive Average Values')
# if is_check7:
#     st.title('Interactive Average Values')
#     # columns1 = data.columns.sort_values().unique().tolist()
#     # columns2 = data.columns.sort_values().unique().tolist()
#
#     # f_attributes1 = st.select_slider('Enter columns',options=columns1)
#     #
#     # #f_attributes2 = st.select_slider('Enter columns',options=columns2)
#     f_attributes1 = st.multiselect('Enter columns', data.columns)
#
#     if f_attributes1 !=[]:
#         data = data.loc[data[f_attributes1]]
#
#     else:
#         data = data.copy()
#     # select rows
#     dteste = data[data.loc[data.columns] == data.loc[data[f_attributes1]]]
#                   #& (columns2 == f_attributes2)].copy()
#
#     st.dataframe(dteste)
#
#     # df2 = data[['id', 'nivel']].groupby('nivel').count().reset_index()
#     # df3 = data[['price', 'nivel']].groupby('nivel').mean().reset_index()
#     # # Merge
#     # m1 = pd.merge(df2, df3, on='nivel', how='inner')



