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
   
    
    listColumn = [ School.city,
            School.globalRating,
            School.successRate,
            School.mentionRate,
            City.name,City.population,
            City.latitude,
            City.longitude
            ]

    #query = School.select(*listColumn).join(City).order_by(-School.globalRating)
    query = School.select(School,City).join(City).order_by(-School.globalRating)
    # query to df
    dfschool =  pd.DataFrame(list(query.dicts()))

    # print 
    #print(dfschool)

    # plot
    dfschool['globalRating'] = dfschool['globalRating'].astype(float) 
    dfschool.plot.bar(x="name" , y="globalRating")
    pyplot.show()
    