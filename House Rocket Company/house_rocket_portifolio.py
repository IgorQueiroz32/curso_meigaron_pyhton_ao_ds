import pandas as pd
import numpy as np
from matplotlib import pyplot
data = pd.read_csv('kc_house_data.csv')

# excluding outliers
data.drop(data[data['bedrooms']>11].index,inplace=True)
data.drop(data[(data['bedrooms']==0) | (data['bathrooms']==0)].index,inplace=True)

# data transformation
pd.set_option('display.float_format', lambda x: '%.3f' % x)
data['waterfront'] = data['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

#solving first question first part
price_median= data[['price', 'zipcode']].groupby('zipcode').median().reset_index()
price_median.columns = ['zipcode', 'price_median']
houses_to_buy = pd.merge(data,price_median,on='zipcode',how='inner')

for i in range(len(houses_to_buy)):
    if (houses_to_buy.loc[i, 'price']<houses_to_buy.loc[i,'price_median']) & (houses_to_buy.loc[i,'condition']>=3):
        houses_to_buy.loc[i,'status'] = 'buy'
        
    else:
        houses_to_buy.loc[i,'status'] = 'do not buy'
        
first_column = houses_to_buy.pop('status')
houses_to_buy.insert(0,'status',first_column)


for i in range(len(houses_to_buy)):
    if (houses_to_buy.loc[i,'bedrooms'] >= 8) | (houses_to_buy.loc[i,'sqft_lot']>=1074218) | (houses_to_buy.loc[i,'bathrooms']>=4.25):
        houses_to_buy.loc[i,'recommendation_to_buy'] = 'very_high'
        
    elif (houses_to_buy.loc[i, 'floors'] >= 2) & (houses_to_buy.loc[i,'bedrooms']>=4) & (houses_to_buy.loc[i,'bedrooms']<=7) & (houses_to_buy.loc[i,'bathrooms']>=2) & (houses_to_buy.loc[i,'bathrooms']<=4):
        houses_to_buy.loc[i,'recommendation_to_buy'] = 'high'
        
    else:
        houses_to_buy.loc[i, 'recommendation_to_buy'] = 'regular'

houses_rec_to_buy = houses_to_buy[houses_to_buy['status'] == 'buy']        
houses_rec_to_buy = houses_rec_to_buy.drop('status', axis=1)

first_column1 = houses_rec_to_buy.pop('recommendation_to_buy')
houses_rec_to_buy.insert(0,'recommendation_to_buy',first_column1)

x = houses_rec_to_buy[(houses_rec_to_buy['id'] == 125059138) | (houses_rec_to_buy['id'] == 125059179) | (houses_rec_to_buy['id'] == 125059178)]
