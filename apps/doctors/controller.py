from connect.connect import db
import settings

from apps.doctors import doctors
from apps.doctors.model  import Doctor
from apps.cities.model  import City
from apps.utils.utils import renameColDataframe, sort_cities_by_field
import pandas as pd 
from matplotlib import  pyplot


def import_doctors_csv_table():    

    # import csv schools
    dfDoctors = doctors.read_doctors_csv_data(settings.PATH_CSV_FILE_DOCTORS)    

    dfDoctors = doctors.add_calculated_column(dfDoctors)

    dataW = doctors.regroupDistrict(dfDoctors,'city')
    result = dataW.groupby(['city'] , as_index=False).sum()
    

    # df to dict 
    DictDoctors =  result.to_dict(orient='records')
    

    # connection db 
    db.connect() 
    # create Table via Model 
    Doctor.create_table()    
    # moulinette csv to db table
    Doctor.insert_many(DictDoctors).execute()
    #show table 

    print('called the right thing in Doctors !!!')

    db.close()

def read_data_from_table():
   

    query = Doctor.select(Doctor,City).join(City)
    # query to df
    dfDoctors =  pd.DataFrame(list(query.dicts()))
    #print(dfDoctors)
    
    dfDoctors['rate'] =  dfDoctors['population'] / dfDoctors['countDoctor']

    dfDoctors['rate'] = dfDoctors['rate'].astype(float)
    dfDoctors['countDoctor'] = dfDoctors['countDoctor'].astype(float)
    dfDoctors.rate = dfDoctors.rate.round(2)
    dfDoctors = dfDoctors.sort_values(by='rate', ascending=False) 
    
    print(dfDoctors)
   
    dfDoctors['population'] /= 10
    dfDoctors['countDoctor'] *= 5
    dfDoctors.plot.bar(x="name" , y=["rate", "countDoctor", "population"])

    pyplot.show()
    