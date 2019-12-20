import settings 
import pandas as pd 
from apps.cities import app as cities
import numpy as np 


#-------------------------------------------------

def read_highschools_csv_data(path):
    data = pd.read_csv(path, low_memory=False, sep=";")
    data['Taux_Mention_brut_toutes_series'] = data['Taux_Mention_brut_toutes_series'].astype(float)
    data['Taux Brut de Réussite Total séries'] = data['Taux Brut de Réussite Total séries'].astype(float)
    #print(data.head().to_string())
    return data

#-------------------------------------------------

def update_field(col, data, criteria, updateValue):
    
    result = data.copy()
    
    result.update({col :    np.where (
            data[col].isin(criteria),
            updateValue,
            data[col]
        )})
    
    return result    

# To trash but to test before
def borough_concatenation(data):

    dataW = regroupDistrict(data,'Code commune')
    result = dataW.groupby(['Code commune'] , as_index=False).agg({'Effectif de seconde' : 'sum'  })

    return result

def borough_concatenation_school(data):

    dataW = regroupDistrict(data,'Code commune')
    result = dataW.groupby(['Code commune'] , as_index=False).mean()

    return result


def regroupDistrict (data,column_name) :
    for key , city in settings.CITIES.items() : 
       data = update_field(column_name, data, city['arr'], city['target']) 

    # data = data.groupby([column_name] , as_index=False).agg({'Taux Brut de Réussite Total séries' : 'mean', 'Taux_Mention_brut_toutes_series' : 'mean'})
    data = data.groupby([column_name] , as_index=False).mean()
    return data

def mergeDataframes (leftDF, rightDF, column_name) :
    return pd.merge(leftDF, rightDF, on=column_name)

def add_calculated_column(data):
    
    data['Score'] = ( data['Taux Brut de Réussite Total séries']  +  data['Taux_Mention_brut_toutes_series']  ) / 10
    #data['Score'] = data.apply(lambda col: (int( col['Taux Brut de Réussite Total séries'] ) + ( int(col['Taux_Mention_brut_toutes_series']) * 2) )  / 3, axis=1)
    return data

def sortByPopulation(data):
    
    return data
    