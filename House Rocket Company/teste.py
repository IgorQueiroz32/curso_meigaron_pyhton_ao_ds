import pandas as pd

# read data
# @st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data
#data2 = pd.read_csv(path)
# Load data
path = 'C:/spyder python/curso meigaron python ds/projetos portifolio/insight/House Rocket Company/kc_house_data.csv'
data = get_data('C:/spyder python/curso meigaron python ds/projetos portifolio/insight/House Rocket Company/kc_house_data.csv')
#data2 = get_data('C:/spyder python/projetos portifolio/insight/House Rocket Company/df2.csv')

# data['is_waterfront'] = data['waterfront'].apply(lambda: 'yes' if x ==1 else 'no')



print(data.shape)