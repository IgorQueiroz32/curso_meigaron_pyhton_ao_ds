import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
import ipywidgets as widgets
from matplotlib import gridspec
from matplotlib import pyplot as plt
from ipywidgets import fixed
import ipywidgets as ipywidgets
from ipywidgets import Box


def show_dtypes(base):
    print(base.dtypes)
    return None


def show_dimensions(base):
    # base dimensions
    print('NUmber of Rows: {}'.format(base.shape[0]))
    print('NUmber of Columns: {}'.format(base.shape[1], end='\n\n'))
    return None


def show_missing_values(base):
    print(pd.isnull(base).sum())
    return None


def update_map_1(base, e_limit):
    df = base[base['Event'] == e_limit].copy()

    fig = plt.figure(figsize=(21, 12))
    specs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig)

    ax1 = fig.add_subplot(specs[0, :])
    ax2 = fig.add_subplot(specs[1, :])
    ax3 = fig.add_subplot(specs[2, :])

    by_year_week = df[['Id', 'year_week']].groupby('year_week').count().reset_index()
    ax1.bar(by_year_week['year_week'], by_year_week['Id'])
    ax1.set_title('title: Number of People at Event by year_week')

    by_year = df[['Id', 'year']].groupby('year').count().reset_index()
    ax2.bar(by_year['year'], by_year['Id'])
    ax2.set_title('title: Number of People at Event by year')

    by_month = df[['Id', 'month']].groupby('month').count().reset_index()
    ax3.bar(by_month['month'], by_month['Id'])
    ax3.set_title('title: Number of People at Event by month')

    return base


def update_map_2(base, e_limit, n_limit):
    df = base[(base['Event'] == e_limit) &
              (base['Name'] == n_limit)].copy()

    fig = plt.figure(figsize=(21, 12))
    specs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig)

    ax1 = fig.add_subplot(specs[0, :])
    ax2 = fig.add_subplot(specs[1, :])
    ax3 = fig.add_subplot(specs[2, :])

    by_year_week = df[['Id', 'year_week']].groupby('year_week').count().reset_index()
    ax1.bar(by_year_week['year_week'], by_year_week['Id'])
    ax1.set_title('title: Number of People at Event by year_week')

    by_year = df[['Id', 'year']].groupby('year').count().reset_index()
    ax2.bar(by_year['year'], by_year['Id'])
    ax2.set_title('title: Number of People at Event by year')

    by_month = df[['Id', 'month']].groupby('month').count().reset_index()
    ax3.bar(by_month['month'], by_month['Id'])
    ax3.set_title('title: Number of People at Event by month')

    return base


# load dataset
base = pd.read_csv('C:/spyder python/study case/Data Analyst CAse Study_May 2021.csv')

# base dimensions
show_dimensions(base)

# base type
show_dtypes(base)

# missing_values
show_missing_values(base)

# creating new attributes
base['Id'] = base.index
base['year'] = pd.to_datetime(base['Date']).dt.strftime('%Y')
base['month'] = pd.to_datetime(base['Date']).dt.strftime('%m')
base['year_week'] = pd.to_datetime(base['Date']).dt.strftime('%Y-%U')

# Filling up missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
base['Current Type'] = imputer.fit_transform(base[['Current Type']])

imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
base['Current Nurturing'] = imputer.fit_transform(base[['Current Nurturing']])

# excluding attributes
base.drop(['Description'], 1, inplace=True)
print(base.head())

# converting object to date
base['Date'] = pd.to_datetime(base['Date'])

show_dimensions(base)

show_dtypes(base)

show_missing_values(base)

# Creating insights
event_per_person = base[['Event', 'Name']].groupby('Name')

person_per_event = base[['Name', 'Event']].groupby('Event')

person_event_date = base[['Event', 'Name', 'Date']].groupby('Date')

# Creating interactive buttons

Event_limit = widgets.Dropdown(
    options=base['Event'].sort_values().unique().tolist(),
    value='Lead Created',
    description='Event',
    disable=False)
Event_limit

Name_limit = widgets.Dropdown(
    options=base['Name'].sort_values().unique().tolist(),
    value='Latesha Labree',
    description='Name',
    disable=False)
Name_limit

# Showing base
# for Date, frame in person_event_date:
#    print (frame.head(5), end='\n\n')
#
# for Name, frame in event_per_person:
#    print (frame.head(5), end='\n\n')
#
# print(base[['Event', 'Name']].groupby('Name').count().reset_index())
#
# print(base[['Name','Event']].groupby('Event').count().reset_index())
#
# print(base[['Name','Current Type']].groupby('Current Type').count().reset_index())
#
# print(base[['Event','Current Nurturing']].groupby('Current Nurturing').count().reset_index())
#
# print(base[['Event', 'Name', 'Date']].groupby('Date').count().reset_index())
#
# print(base[['Event', 'Name']][base['Name'] == 'Aaron Banks'])
#
# print(base[['Event', 'Name']][base['Event'] == 'Lead Pipeline Update'])

interactive_update_map_1 = widgets.interactive(update_map_1, base=fixed(base), e_limit=Event_limit)

interactive_update_map_2 = widgets.interactive(update_map_2, base=fixed(base), e_limit=Event_limit, n_limit=Name_limit)

items = [interactive_update_map_1, interactive_update_map_2]
box = Box(children=items, layout=ipywidgets.Layout(display="flex", flex_flow="column", align_items="stretch"))
box