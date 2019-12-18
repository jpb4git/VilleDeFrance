from connect.connect import db
import settings
from apps.cities.cities import read_cities_csv_data  
from apps.cities.model  import City
from apps.utils.utils import renameColDataframe , sort_cities_by_field
def import_csv_table(): 
    

    # import csv cities
    dfCities = read_cities_csv_data(settings.PATH_CSV_FILE)    
    dfCities =  sort_cities_by_field(dfCities,'13').head(50)
    # connection db 
    db.connect()
    
    # drop table 
    #db.drop_tables(City)
    
    # create Table via Model 
    City.create_table()    
    
    #rename columns
    dfCities = renameColDataframe(dfCities,{'4':'name', '9':'insee', '13':'population','17' : 'longitude','18' : 'latitude'})    
    dfCities = dfCities[['name','insee','population','longitude','latitude']]

    # df to dict 
    DictCities =  dfCities.to_dict(orient='records')
    
    # moulinette csv to db table
    City.insert_many(DictCities).execute()
    #show table 

    print('called the right thing !!!')

    db.close()