import settings 
import pandas as pd 
from apps.cities import cities
import numpy as np 

def read_doctors_csv_data(path):
    data = pd.read_csv(path, low_memory=False, sep=",")
    data = data[['c_depcom']]
    return data


# To trash but to test before
def borough_concatenation(data):

    dataW = regroupDistrict(data,'c_depcom')

    result = dataW.groupby(['c_depcom'] , as_index=False).sum()

    return result

def regroupDistrict (data,column_name) :
    for key , city in settings.CITIES.items() : 
       data = update_field(column_name, data, city['arr'], city['target']) 

    # data = data.groupby([column_name] , as_index=False).agg({'Taux Brut de Réussite Total séries' : 'mean', 'Taux_Mention_brut_toutes_series' : 'mean'})
    data = data.groupby([column_name] , as_index=False).sum()
    return data

def update_field(col, data, criteria, updateValue):
    
    result = data.copy()
    
    result.update({col :    np.where (
            data[col].isin(criteria),
            updateValue,
            data[col]
        )})
    
    return result    

def add_calculated_column(data): 
    data['countDoctor'] = 1
    return data