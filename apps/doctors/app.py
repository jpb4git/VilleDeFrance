import settings 
import pandas as pd 
from apps.cities import app as cities
from apps.utils import app as utils
import numpy as np 

def read_doctors_csv_data(path):
    data = pd.read_csv(path, low_memory=False, sep=",")
    data = data[['c_depcom']]
    
    return utils.renameColDataframe(data, {'c_depcom' : 'city'})


# To trash but to test before
def borough_concatenation(data):

    dataW = regroupDistrict(data,'city')

    result = dataW.groupby(['city'] , as_index=False).sum()

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

def add_calculated_column(data, colname): 
    data[colname] = 1
    return data

def add_calculated_rate_column(data, colname): 
    data[colname] = data['population'] / data['countDoctors']
    return data
