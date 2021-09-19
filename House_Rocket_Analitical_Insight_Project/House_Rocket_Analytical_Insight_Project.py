import    pandas as pd
import streamlit as st
import    plotly.express as px

st.set_page_config(layout='wide')# deixa a tabela no site maior, mais larga

# read data
@st.cache(allow_output_mutation=True) # funcao q permite ler os dados da memoria virtual
def get_data(path):
    data = pd.read_csv(path)

    return data

# transformation

# excluding outliers
def data_excluding(data):
    data.drop(data[data['bedrooms']>11].index,inplace=True)
    data.drop(data[(data['bedrooms']==0) | (data['bathrooms']==0)].index,inplace=True)
    data.drop(data[(data['id']==125059179) | (data['id']==125059178)].index,inplace=True)

    return data

# data transformation
def set_feature(data):
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data['month_day'] = pd.to_datetime(data['date']).dt.strftime('%m-%d')

    return data

def houses_buy(data):
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

    st.header(houses_to_buy.shape)
    st.write('Num of Houses, Num of Attributes')
    st.dataframe(houses_to_buy)

    st.write("This table informs which house is indicated to buy, among 21594 houses available. Also it presents all houses characteristics.")

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

    return houses_to_buy

def houses_sell(houses_to_buy):
    # solving second question first part (for how much the houses should be sold)
    houses_buy_sell = houses_to_buy
    houses_buy_sell = houses_buy_sell[houses_buy_sell.status == 'buy']
    houses_buy_sell = houses_buy_sell.drop('status', axis=1)

    first_column1 = houses_buy_sell.pop('recommendation_to_buy')
    houses_buy_sell.insert(0, 'recommendation_to_buy', first_column1)

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

    return houses_buy_sell

def profits(houses_buy_sell):
    # solving second question second part (when sell the houses)
    for i in range(len(houses_buy_sell)):
        houses_buy_sell.loc[i, 'profit'] = (houses_buy_sell.loc[i, 'price_to_sell']) - (houses_buy_sell.loc[i, 'price'])

    first_column3 = houses_buy_sell.pop('profit')
    houses_buy_sell.insert(5, 'profit', first_column3)

    for i in range(len(houses_buy_sell)):
        houses_buy_sell.loc[i, 'profit_percentage_per_house'] = (((houses_buy_sell.loc[i, 'price_to_sell']) - (
        houses_buy_sell.loc[i, 'price'])) / houses_buy_sell.loc[i, 'price']) * 100

    first_column4 = houses_buy_sell.pop('profit_percentage_per_house')
    houses_buy_sell.insert(6, 'profit_percentage_per_house', first_column4)

    for i in range(len(houses_buy_sell)):
        houses_buy_sell.loc[i, 'profit_percentage_total'] = ((houses_buy_sell.loc[i, 'profit']) / (
            houses_buy_sell['profit'].sum())) * 100

    first_column5 = houses_buy_sell.pop('profit_percentage_total')
    houses_buy_sell.insert(7, 'profit_percentage_total', first_column5)

    return houses_buy_sell

def map(houses_buy_sell):
    # entire dataframe of houses to buy
    f_recommendation_to_buy = st.sidebar.multiselect('Enter Houses Recommendation to Buy',
                                       houses_buy_sell['recommendation_to_buy'].sort_values().unique())

    if f_recommendation_to_buy != []:
        houses_buy_sell_df = houses_buy_sell.loc[houses_buy_sell['recommendation_to_buy'].isin(f_recommendation_to_buy)]

    else:
        houses_buy_sell_df = houses_buy_sell.copy()

    st.header(houses_buy_sell_df.shape)
    st.write('Num of Houses, Num of Attributes')
    st.dataframe(houses_buy_sell_df)
    st.write("Here the table is organized by houses recommendation, such as:")
    st.write("Very high - 19 houses available with number of bedrooms above 8, size above 1074218 sqft and number of bathrooms above 8.")
    st.write("High - 755 houses available with number of floors greater or equal to 2, number of bedrooms between 4 and 7, and number of bathrooms between 2 and 4.")
    st.write("Regular - 9797 houses available.")

    # plot map
    houses_sell = houses_buy_sell[['recommendation_to_buy', 'condition', 'bedrooms', 'bathrooms', 'waterfront', 'lat', 'long', 'price']]
    high = houses_sell[(houses_sell['recommendation_to_buy'] == 'high') & (houses_sell['condition'] > 3)]

    reg = houses_sell[(houses_sell['condition'] == 5) & (houses_sell['recommendation_to_buy'] == 'regular') & (houses_sell['bedrooms'] >= 4) & (houses_sell['bathrooms'] >= 2) | (houses_sell['waterfront'] == 1)]

    v_high = houses_sell[houses_sell['recommendation_to_buy'] == 'very_high']

    rec1 = high.append(reg)
    rec2 = rec1.append(v_high)

    if f_recommendation_to_buy != []:
        houses_buy_sell_map = rec2.loc[rec2['recommendation_to_buy'].isin(f_recommendation_to_buy)]

    else:
        houses_buy_sell_map = rec2.copy()

    st.header('Portfolio Map')
    dfm = houses_buy_sell_map[['lat', 'long', 'condition', 'price']]
    st.header(dfm.shape)
    st.write('Num of Houses, Num of Attributes')

    fig = px.scatter_mapbox(dfm,
                            lat = 'lat',
                            lon = 'long',
                            color = 'condition',
                            size = 'price',
                            color_continuous_scale = 'Bluered_r',
                            size_max = 15,
                            zoom = 10)

    fig.update_layout(mapbox_style = 'open-street-map')
    fig.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
    st.plotly_chart(fig)
    st.write("The map above shows houses that are also organized by the recommendation_to_buy attribute, however the values of these attributes are more filtered, where:")
    st.write("Very high - 19 houses available; no water view.")
    st.write("High - 124 houses available with condition above 3; no water view.")
    st.write("Regular - 111 available houses with condition equal to 5, number of bedrooms above 3, number of bathrooms greater or equal to 2. Also includes some houses that are not within the above characteristics, but have water view.")

    return None

def time_sell(houses_buy_sell):

    time_to_sell = houses_buy_sell[['profit', 'profit_percentage_total', 'season']].groupby(
        ['season']).sum().reset_index()
    time_to_sell.columns = ['season', 'profit', 'profit_percentage_total']

    df1 = houses_buy_sell[['profit', 'season', 'recommendation_to_buy', 'profit_percentage_total']].groupby(
        ['season', 'recommendation_to_buy']).sum().reset_index()
    df2 = houses_buy_sell[['id', 'season', 'recommendation_to_buy']].groupby(
        ['season', 'recommendation_to_buy']).count().reset_index()
    gen_ind_profit = pd.merge(df1, df2, how='inner')

    for i in range(len(gen_ind_profit)):
        gen_ind_profit.loc[i, 'profit_each_house'] = (gen_ind_profit.loc[i, 'profit']) / (gen_ind_profit.loc[i, 'id'])

    gen_ind_profit.columns = ['season', 'recommendation_to_buy', 'total_profit', 'profit_percentage_total',
                              'num_of_houses', 'mean_profit_each_house']

    total_price = houses_buy_sell['price'].sum()
    total_profit = houses_buy_sell['profit'].sum()
    total = pd.DataFrame([[total_price, total_profit]], columns=['total_price', 'total_profit'])
    for i in range(len(total)):
        total.loc[i, 'profit_percentage'] = ((total.loc[i, 'total_profit']) / (total.loc[i, 'total_price'])) * 100

    st.header('Best Moment to Sell')
    st.dataframe(time_to_sell)
    st.write("According this table, summer presents the highest amount of profit, with more than 30 percent, so it is the best moment to sell houses.")

    st.header('General and Individual Profit')
    st.dataframe(gen_ind_profit, height=800)
    st.write("Here it is possible to identify the houses profit by season and houses recommendation, also the table shows the mean profit made by each house. ")
    st.write("This table informs that regular houses make the highest profit than the others recommendations in every season, flouting between 15.5 and 27.5 percent, with summer presenting the highest profit and winter the lowest.")
    st.write("However, dividing the profit by the number of houses, both related to each type of house recommendation, houses very high recommended presents the highest profit among all recommendations. Where summer is at first position with $138675,00 of profit per house; and winter at last position with $88,262.1429.")

    st.header('Total Profit Percentage')
    st.dataframe(total)
    st.write("This table represents the total profit by buying and selling all houses recommended buying. It informs that, by following this project, the company would have a profit of almost 19 percent, which are more than $771 million.")

    return None

def hypothesis(houses_to_buy):
    st.title('Hypotheses')
    st.write('Those hypotheses include all houses from dataset, house to buy and houses not to buy.')

    #Hypothesis 01
    st.header('Hypothesis 01: Houses with water view are 20% more expensive, on the average.')

    dfh1 = houses_to_buy[['waterfront', 'price']]
    for i in range(len(dfh1)):
        if (dfh1.loc[i, 'waterfront'] == 1):
            dfh1.loc[i, 'water_view'] = 'yes'

        else:
            dfh1.loc[i, 'water_view'] = 'no'

    h1 = dfh1[['price', 'water_view']].groupby('water_view').mean().reset_index()
    # (produto mais caro - produto mais barato)  / produto mais barato * 100
    h1_answer = ((h1.loc[1, 'price']) - (h1.loc[0, 'price'])) / (h1.loc[0, 'price']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h1, x='water_view', y='price', color='water_view')
    c1.plotly_chart(fig, use_container_width=True)


    c2.dataframe(h1)
    st.write('False: Houses with water view are {} percent more expensive.'.format(h1_answer))


    #Hypothesis 02
    st.header('Hypothesis 02: Houses that was built before 1955 are 50% cheaper, on the average.')

    dfh2 = houses_to_buy[['yr_built', 'price']]

    for i in range(len(dfh2)):
        if (dfh2.loc[i, 'yr_built'] >= 1955):
            dfh2.loc[i, 'yr_built_1955'] = 'after'

        else:
            dfh2.loc[i, 'yr_built_1955'] = 'before'

    h2 = dfh2[['price', 'yr_built_1955']].groupby('yr_built_1955').mean().reset_index()

    # (produto mais barato - produto mais caro)  / produto mais caro * 100
    h2_answer = ((h2.loc[1, 'price']) - (h2.loc[0, 'price'])) / (h2.loc[0, 'price']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h2, x='yr_built_1955', y='price', color='yr_built_1955')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h2)
    st.write('False: Houses that was built before 1955 are {} percent cheaper.'.format(h2_answer))


    # Hypothesis 03
    st.header('Hypothesis 03: Houses without basement are 40% bigger than house with basement, related to total area (sqft_lot), on average.')

    dfh3 = houses_to_buy[['sqft_basement', 'sqft_lot']]

    for i in range(len(dfh3)):
        if (dfh3.loc[i, 'sqft_basement'] == 0):
            dfh3.loc[i, 'basement'] = 'No'

        else:
            dfh3.loc[i, 'basement'] = 'Yes'

    h3 = dfh3[['sqft_lot', 'basement']].groupby('basement').mean().reset_index()

    # (produto maior - produto menor)  / produto menor  * 100
    h3_answer = ((h3.loc[0, 'sqft_lot']) - (h3.loc[1, 'sqft_lot'])) / (h3.loc[1, 'sqft_lot']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h3, x='basement', y='sqft_lot', color='basement')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h3)
    st.write('False: Houses without basement are {} percent bigger them houses with basement.'.format(h3_answer))


    # Hypothesis 04
    st.header('Hypothesis 04: The increase of houses price YoY (Year over Year) (May 2014 compared to May 2015) is 10%, in general.')
    #Houses price of may 2014 compared to Houses price of may 2015
    #COMPOUND ANNUAL GROWTH RATES (CAGR)

    dfh4 = houses_to_buy[['date', 'price']]

    dfh4['year_month'] = pd.to_datetime(dfh4['date']).dt.strftime('%Y-%m')

    dfh4 = dfh4[(dfh4['year_month'] == '2014-05') | (dfh4['year_month'] == '2015-05')]

    h4 = dfh4[['price', 'year_month']].groupby('year_month').sum().reset_index()

    h4.columns = ['year_month', 'sum_of_price']

    # taxa de crescimento mensal simple, mes por mes
    # (esse ano - ano passado) / ano passado
    h4_answer = ((h4.loc[1, 'sum_of_price']) - (h4.loc[0, 'sum_of_price'])) / (h4.loc[0, 'sum_of_price']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h4, x='year_month', y='sum_of_price', color='year_month')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h4)
    st.write('False: The total houses price YoY (Year over Year) suffered a decrease of {} percent.'.format(h4_answer))


    # Hypothesis 05
    st.header('Hypothesis 05: Houses with 3 bathrooms have an increase MoM (month over Month) of 15%, in general.')
    #comparison of all Houses price of all months
    #COMPOUND MONTHLY GROWTH RATES (CMGR)

    dfh5 = houses_to_buy[['date', 'price', 'bathrooms']]

    dfh5['year_month'] = pd.to_datetime(dfh5['date']).dt.strftime('%Y-%m')

    dfh5 = dfh5[(dfh5['bathrooms'] == 3)]

    h5 = dfh5[['price', 'year_month']].groupby('year_month').sum().reset_index()

    h5.columns = ['year_month', 'sum_of_price']

    # taxa de crescimento mensal simple, mes por mes
    # (esse mes - mes passado) / mes passado
    h5['MoM_percentage'] = ((h5['sum_of_price'] - h5['sum_of_price'].shift(1)) / h5['sum_of_price'].shift(1)) * 100

    # taxa de crescimento mensal composta, o ultimo mes pelo primeiro mes contando todos os meses do meio
    # (last/first)**(1/periods)-1
    cmgr = (((h5.loc[12, 'sum_of_price']) / (h5.loc[0, 'sum_of_price'])) ** (
                1 / (h5['sum_of_price'].count() - 1)) - 1) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.line(h5, x='year_month', y='sum_of_price')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h5)
    st.write('False: The total houses price MoM (month over Month) suffered a decrease of {} percent.'.format(cmgr))


    # Hypothesis 06
    st.header('Hypothesis 06: Houses with number of bedrooms above 8 have a number of bathrooms 40% higher than houses with number of bedrooms between 5 and 8, and 94% higher than houses with number of bedrooms between 1 and, 4 on average.')

    dfh6 = houses_to_buy[['bedrooms', 'bathrooms']]

    for i in range(len(dfh6)):
        if (dfh6 .loc[i, 'bedrooms'] > 8):
            dfh6 .loc[i, 'bedrooms_level'] = 3

        elif (dfh6 .loc[i, 'bedrooms'] >= 5) & (dfh6 .loc[i, 'bedrooms'] <= 8):
            dfh6 .loc[i, 'bedrooms_level'] = 2

        else:
            dfh6 .loc[i, 'bedrooms_level'] = 1

    h6 = dfh6[['bathrooms', 'bedrooms_level']].groupby('bedrooms_level').mean().reset_index()

    # (produto maior - produto menor)  / produto menor  * 100
    for i in range(len(h6)):
        h6.loc[i, 'percentage'] = ((h6.loc[2, 'bathrooms'] - h6.loc[i, 'bathrooms']) / h6.loc[i, 'bathrooms']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h6, x='bedrooms_level', y='bathrooms', color='bedrooms_level')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h6)
    st.write('True: Houses with number of bedrooms above 8 have a number of bathrooms {} percent higher than houses with number of bedrooms between 5 and 8, and {} higher than houses with number of bedrooms between 1 and 4.'.format(h6.iloc[1,2],h6.iloc[0,2]))
    # Hypothesis 07
    st.header('Hypothesis 07: Houses with 7 bedrooms has the total area (sqft_lot) bigger between 132 to 320 percent than houses with 8 to 11 bedrooms, on average.')

    dfh7 = houses_to_buy[['bedrooms', 'sqft_lot']]

    h7 = dfh7[['bedrooms', 'sqft_lot']].groupby('bedrooms').mean().reset_index()

    # (produto maior - produto menor)  / produto menor  * 100
    for i in range(len(h7)):
        h7.loc[i, 'percentage'] = ((h7.loc[6, 'sqft_lot'] - h7.loc[i, 'sqft_lot']) / h7.loc[i, 'sqft_lot']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.line(h7, x='bedrooms', y='sqft_lot')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h7)
    st.write('True: Houses with 7 bedrooms has the total area (sqft_lot) bigger between {} and {} percent than houses with 8 to 11 bedrooms.'.format(h7.iloc[7,2],h7.iloc[10,2]))


    # Hypothesis 08
    st.header('Hypothesis 08: Renovated Houses have living rooms 12% bigger than house not renovated, on average.')

    dfh8 = houses_to_buy[['sqft_living', 'yr_renovated']]

    for i in range(len(dfh8)):
        if (dfh8.loc[i, 'yr_renovated'] == 0):
            dfh8.loc[i, 'renovated'] = 'No'

        else:
            dfh8.loc[i, 'renovated'] = 'Yes'

    h8 = dfh8[['sqft_living', 'renovated']].groupby('renovated').mean().reset_index()

    # (produto maior - produto menor)  / produto menor  * 100
    h8_answer = ((h8.loc[1, 'sqft_living']) - (h8.loc[0, 'sqft_living'])) / (h8.loc[0, 'sqft_living']) * 100

    c1, c2 = st.beta_columns((1, 1))
    fig = px.bar(h8, x='renovated', y='sqft_living', color='renovated')
    c1.plotly_chart(fig, use_container_width=True)

    c2.dataframe(h8)
    st.write('True: Renovated Houses have living rooms {} percent bigger than houses not renovated, on average.'.format(h8_answer))

    st.title('Conclusion')
    st.write('In conclusion, it is possible to identify that the application of data analytics project at dataset from House Rocket Company was very successful, providing a huge profit opportunity based on which houses to buy and when to sell.')

    st.title('Next Steps')
    st.write('Other project that can be made with this dataset is the exploration data analyses, which identify the best’s attributes in order to apply machine learning algorithms, with the objective to predict the price of futures houses to buy.')
    return None

if __name__=="__main__":
    #ETL
    # data extraction
    path = 'kc_house_data.csv'
    data = get_data(path)

    #transformatiom
    data = data_excluding(data)

    data = set_feature(data)

    x = houses_buy(data)

    y = houses_sell(x)

    z = profits(y)

    map(z)

    time_sell(z)

    hypothesis(x)