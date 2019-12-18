from connect.connect import db
import settings
from apps.school.school import read_highschools_csv_data, borough_concatenation_school, add_calculated_column  
from apps.school.model  import School
from apps.utils.utils import renameColDataframe, sort_cities_by_field


def import_school_csv_table():    

    # import csv schools
    dfSchools = read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)    

    # connection db 
    db.connect()
    
    # drop table 
    #db.drop_tables(School)
    
    # create Table via Model 
    School.create_table()    

    # Group schools by district
    dfSchools = borough_concatenation_school(dfSchools)
    
    # Calculate and add Score column
    dfSchools = add_calculated_column(dfSchools)

    #rename columns
    dfSchools = renameColDataframe(dfSchools,{'Code commune':'insee','Taux_Mention_brut_toutes_series':'mentionRate', 'Taux Brut de Réussite Total séries':'successRate', 'Score':'globalRating'})    
    dfSchools = dfSchools[['insee','mentionRate','successRate','globalRating']]



    # df to dict 
    DictSchools =  dfSchools.to_dict(orient='records')
    print(DictSchools)
    
    # moulinette csv to db table
    School.insert_many(DictSchools).execute()
    #show table 

    print('called the right thing in school !!!')

    db.close()