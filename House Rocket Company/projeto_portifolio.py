import    pandas as pd
import streamlit as st
import     numpy as np
import    plotly.express as px

st.set_page_config(layout='wide')# deixa a tabela no site maior, mais larga

# read data
@st.cache(allow_output_mutation=True) # funcao q permite ler os dados da memoria virtual
def get_data(path):
    data = pd.read_csv(path)

    return data

# Load data
path = 'kc_house_data.csv'
data = get_data(path)

# transformation

# excluding outliers
data.drop(data[data['bedrooms']>11].index,inplace=True)
data.drop(data[(data['bedrooms']==0) | (data['bathrooms']==0)].index,inplace=True)
data.drop(data[(data['id']==125059179) | (data['id']==125059178)].index,inplace=True)

# data transformation
pd.set_option('display.float_format', lambda x: '%.3f' % x)
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
data['month_day'] = pd.to_datetime(data['date']).dt.strftime('%m-%d')

st.title('House Rocket Company')
st.markdown('Welcome to House Rocket Data Analysis')

# solving first question (which houses should be bought)
st.header('Houses to Buy')

price_median_buy = data[['price', 'zipcode']].groupby('zipcode').median().reset_index()
price_median_buy.columns = ['zipcode', 'price_median_buy']
houses_to_buy = pd.merge(data,price_median_buy,on='zipcode',how='inner')

for i in range(len(houses_to_buy)):
    if (houses_to_buy.loc[i, 'price'] < houses_to_buy.loc[i, 'price_median_buy']) & (
            houses_to_buy.loc[i, 'condition'] >= 3):
        houses_to_buy.loc[i, 'status'] = 'buy'

    else:
        houses_to_buy.loc[i, 'status'] = 'do not buy'

first_column = houses_to_buy.pop('status')
houses_to_buy.insert(0, 'status', first_column)

st.dataframe(houses_to_buy)
st.write("This table informs which house is indicated to buy, also it presents all houses characteristics.")

#solving first question second part
st.header('Houses Recommendation to Buy')

for i in range(len(houses_to_buy)):
    if (houses_to_buy.loc[i, 'bedrooms'] >= 8) | (houses_to_buy.loc[i, 'sqft_lot'] >= 1074218) | (
            houses_to_buy.loc[i, 'bathrooms'] >= 4.25):
        houses_to_buy.loc[i, 'recommendation_to_buy'] = 'very_high'

    elif (houses_to_buy.loc[i, 'floors'] >= 2) & (houses_to_buy.loc[i, 'bedrooms'] >= 4) & (
            houses_to_buy.loc[i, 'bedrooms'] <= 7) & (houses_to_buy.loc[i, 'bathrooms'] >= 2) & (
            houses_to_buy.loc[i, 'bathrooms'] <= 4):
        houses_to_buy.loc[i, 'recommendation_to_buy'] = 'high'

    else:
        houses_to_buy.loc[i, 'recommendation_to_buy'] = 'regular'

for i in range(len(houses_to_buy)):
    if (houses_to_buy.loc[i, 'month_day'] >= '03-01') & (houses_to_buy.loc[i, 'month_day'] <= '05-31'):
        houses_to_buy.loc[i, 'season'] = 'spring'

    elif (houses_to_buy.loc[i, 'month_day'] >= '06-01') & (houses_to_buy.loc[i, 'month_day'] <= '08-31'):
        houses_to_buy.loc[i, 'season'] = 'summer'

    elif (houses_to_buy.loc[i, 'month_day'] >= '09-01') & (houses_to_buy.loc[i, 'month_day'] <= '11-30'):
        houses_to_buy.loc[i, 'season'] = 'fall'

    else:
        houses_to_buy.loc[i, 'season'] = 'winter'

# solving second question first part (for how much the houses should be sold)
houses_buy_sell = houses_to_buy
houses_buy_sell = houses_buy_sell[houses_buy_sell.status == 'buy']
houses_buy_sell = houses_buy_sell.drop('status', axis=1)

first_column1 = houses_buy_sell.pop('recommendation_to_buy')
houses_buy_sell.insert(0,'recommendation_to_buy',first_column1)

price_median_sell = houses_buy_sell[['price', 'zipcode', 'season']].groupby(
    ['zipcode', 'season']).median().reset_index()
price_median_sell.columns = ['zipcode', 'season', 'price_median_sell']
houses_buy_sell = pd.merge(houses_buy_sell, price_median_sell, how='inner')

for i in range(len(houses_buy_sell)):
    if (houses_buy_sell.loc[i, 'price'] < houses_buy_sell.loc[i, 'price_median_sell']) & (
            houses_buy_sell.loc[i, 'recommendation_to_buy'] == 'regular'):
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.3)

    elif (houses_buy_sell.loc[i, 'price'] < houses_buy_sell.loc[i, 'price_median_sell']) & (
            houses_buy_sell.loc[i, 'recommendation_to_buy'] == 'high'):
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.375)

    elif (houses_buy_sell.loc[i, 'price'] < houses_buy_sell.loc[i, 'price_median_sell']) & (
            houses_buy_sell.loc[i, 'recommendation_to_buy'] == 'very_high'):
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.45)

    elif (houses_buy_sell.loc[i, 'price'] > houses_buy_sell.loc[i, 'price_median_sell']) & (
            houses_buy_sell.loc[i, 'recommendation_to_buy'] == 'regular'):
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.10)

    elif (houses_buy_sell.loc[i, 'price'] > houses_buy_sell.loc[i, 'price_median_sell']) & (
            houses_buy_sell.loc[i, 'recommendation_to_buy'] == 'high'):
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.125)

    else:
        houses_buy_sell.loc[i, 'price_to_sell'] = houses_buy_sell.loc[i, 'price'] + (
                    houses_buy_sell.loc[i, 'price'] * 0.15)

first_column2 = houses_buy_sell.pop('price_to_sell')
houses_buy_sell.insert(4, 'price_to_sell', first_column2)

#solving second question second part (when sell the houses)
for i in range(len(houses_buy_sell)):
    houses_buy_sell.loc[i, 'profit'] = (houses_buy_sell.loc[i, 'price_to_sell']) - (houses_buy_sell.loc[i, 'price'])

first_column3 = houses_buy_sell.pop('profit')
houses_buy_sell.insert(5, 'profit', first_column3)

for i in range(len(houses_buy_sell)):
    houses_buy_sell.loc[i,'profit_percentage_per_house'] = (((houses_buy_sell.loc[i,'price_to_sell']) - (houses_buy_sell.loc[i,'price'])) / houses_buy_sell.loc[i,'price']) * 100

first_column4 = houses_buy_sell.pop('profit_percentage_per_house')
houses_buy_sell.insert(6,'profit_percentage_per_house',first_column4)

for i in range(len(houses_buy_sell)):
    houses_buy_sell.loc[i,'profit_percentage_total'] = ((houses_buy_sell.loc[i,'profit']) / (houses_buy_sell['profit'].sum())) * 100

first_column5 = houses_buy_sell.pop('profit_percentage_total')
houses_buy_sell.insert(7,'profit_percentage_total',first_column5)

time_to_sell = houses_buy_sell[['profit', 'profit_percentage_total', 'season']].groupby(['season']).sum().reset_index()
time_to_sell.columns = ['season', 'profit', 'profit_percentage_total']

df1 = houses_buy_sell[['profit', 'season','recommendation_to_buy','profit_percentage_total']].groupby(['season','recommendation_to_buy']).sum().reset_index()
df2 = houses_buy_sell[['id', 'season','recommendation_to_buy']].groupby(['season','recommendation_to_buy']).count().reset_index()
gen_ind_profit = pd.merge(df1,df2,how='inner')

for i in range(len(gen_ind_profit)):
    gen_ind_profit.loc[i,'profit_each_house'] = (gen_ind_profit.loc[i,'profit']) / (gen_ind_profit.loc[i,'id'])

gen_ind_profit.columns = ['season','recommendation_to_buy','total_profit','profit_percentage_total','num_of_houses','mean_profit_each_house']

#criar uma tabela com preco total de compra, total de profit e percentual de diferenca
total_price = houses_buy_sell['price'].sum()
total_profit = houses_buy_sell['profit'].sum()
total = pd.DataFrame([[total_price, total_profit]], columns=['total_price', 'total_profit'])
for i in range(len(total)):
    total.loc[i,'profit_percentage'] = ((total.loc[i,'total_profit']) / (total.loc[i,'total_price'])) * 100

# #plot map
# f_recommendation_to_buy = st.sidebar.multiselect('Enter Houses Recommendation to Buy',
#                                    houses_buy_sell['recommendation_to_buy'].sort_values().unique()) # 3.3.1
#
# if f_recommendation_to_buy != []:
#     houses_buy_sell_map = houses_buy_sell.loc[houses_buy_sell['recommendation_to_buy'].isin(f_recommendation_to_buy)]
#
# else:
#     houses_buy_sell_map = houses_buy_sell.copy()
#
# st.dataframe(houses_buy_sell_map)
# st.write("Here the table is organised by houses recommendation, such as : regular, high and very high. Also it informs other houses characteristics, such as: price to sell, profit, and others.")
#
# st.header('Portfolio Map')
# st.write(" This map shows the location, price and condition of each house.")
# fig = px.scatter_mapbox(houses_buy_sell_map,
#                         lat = 'lat',
#                         lon = 'long',
#                         color = 'condition',
#                         size = 'price',
#                         color_continuous_scale = 'Bluered_r',
#                         size_max = 15,
#                         zoom = 10)
#
# fig.update_layout(mapbox_style = 'open-street-map')
# fig.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
# st.plotly_chart(fig)
#
# st.header('Best Moment to Sell')
# st.dataframe(time_to_sell)
# st.write("According this table, summer presents the highest amount of profit, with more than 30 percent, so it is the best moment to sell houses.")
#
# st.header('General and Individual Profit')
# st.dataframe(gen_ind_profit)
# st.write("Here it is possible to identify the houses profit by season and houses recommendation, also the table shows the mean profit made by each house. ")
# st.write("This table informs that regular houses make the highest profit than the others recommendations in every season, flouting between 15.5 and 27.5 percent, with summer presenting the highest profit andd winter the lowest.")
# st.write("However, dividing the profit by the number of houses, both related to each type of house recommendation, houses very high recommended presents the highest profit among all recommendations. Where summer is at first position with $138675,00 of profit per house; and winter at last position with $88,262.1429.")
#
# st.header('Total Profit Percentage')
# st.dataframe(total)
# st.write("This table represents the total profit by buying and selling all houses recommended to buy. It informs that, by following this project, the company would have a profit of almost 19 percent, Which is more than $771 millions.")
s = data[data['waterfront'] == 'yes']
st.dataframe(s)
st.title('Hypothesis')
c1, c2 = st.beta_columns((1, 1))
st.header('Hypothesis 01: Houses with water view are 20% more expensive, on the average.')
h1 = data[['price', 'waterfront']].groupby('waterfront').mean().reset_index()

# (produto mais caro - produto mais barato)  / produto mais barato * 100
h1_answer = ((h1.loc[1, 'price']) - (h1.loc[0, 'price'])) / (h1.loc[0, 'price']) * 100


fig = px.bar(h1, x='waterfront', y='price')
c1.plotly_chart(fig, use_container_width=True)

c2.dataframe(h1)
st.write('False: Houses with water view are {} percent more expensive'.format(h1_answer))

