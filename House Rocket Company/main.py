# ----------------------------------------
# Libraries
# ---------------------------------------

import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import ipywidgets as widgets
from ipywidgets import fixed
import plotly.express as px
from matplotlib import gridspec
from matplotlib import pyplot as plt
import ipywidgets as ipywidgets
from ipywidgets import Box
import streamlit as st


# ----------------------------------------
# Functions
# ---------------------------------------

def show_dtypes(data):
    print(data.dtypes)
    return None


def show_dimensions(data):
    print('Number of rows: {}'.format(data.shape[0]))
    print('Number of columns: {}'.format(data.shape[1]), end='\n\n')
    return None


def collect_geodata(data, cols):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent='geopiExercises')

    # Creating empty rows
    data.loc[:, cols[0]] = 'NA'
    data.loc[:, cols[1]] = 'NA'
    data.loc[:, cols[2]] = 'NA'
    data.loc[:, cols[3]] = 'NA'
    data.loc[:, cols[4]] = 'NA'
    data.loc[:, cols[5]] = 'NA'
    data.loc[:, cols[6]] = 'NA'
    data.loc[:, cols[7]] = 'NA'
    data.loc[:, cols[8]] = 'NA'

    for i in range(len(data)):
        print('Loop: {}/{}'.format(i, len(data)))

        # make query
        query = str(data.loc[i, 'lat']) + ',' + str(data.loc[i, 'long'])  # concatenadno as duas colunas

        # API Request
        response = geolocator.reverse(
            query)  # fizemos requisicao da API geopy, passando o query acima, que acha o endereco de
        # todas as lst e long

        # populate data
        if cols[0] in response.raw[
            'address']:  # este if significa se tiver a coluna road dentro de address, preenchemos com o lat e long, se nao, pula
            data.loc[i, 'house_number'] = response.raw['address'][cols[0]]

        if cols[1] in response.raw['address']:
            data.loc[i, 'road'] = response.raw['address'][cols[1]]

        if cols[2] in response.raw['address']:
            data.loc[i, 'neighbourhood'] = response.raw['address'][cols[2]]

        if cols[3] in response.raw['address']:
            data.loc[i, 'city'] = response.raw['address'][cols[3]]

        if cols[4] in response.raw['address']:
            data.loc[i, 'county'] = response.raw['address'][cols[4]]

        if cols[5] in response.raw['address']:
            data.loc[i, 'state'] = response.raw['address'][cols[5]]

        if cols[6] in response.raw['address']:
            data.loc[i, 'country'] = response.raw['address'][cols[6]]

        if cols[7] in response.raw:
            data.loc[i, 'place_id'] = response.raw[cols[7]]

        if cols[8] in response.raw:
            data.loc[i, 'osm_type'] = response.raw[cols[8]]

    return data