import settings 
import pandas as pd 
from apps.cities import cities
import numpy as np 
'''
def load_data_school() :
   
    data = pd.read_csv(PATH_CSV_FILE_SCHOOL ,low_memory = False , sep=";" )  
    test= data.sort_values(by=['Ville'], ascending=False)
    
    return test.head(50)
def groupSBInsee() :

    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(PATH_CSV_FILE_SCHOOL ,low_memory = False , sep=";" )  

    #Smelly Code, Smelly code what are they feeding you ?
    #Smelly Code, smelly code it's not your fault...
    #test= data[['Ville'],['Taux Brut de Réussite Total séries']].sort_values(by=['Ville'], ascending=False)
    test= data[['Ville']]
    
    #print(test)
    return test
def groupSchoolByInsee(df) :
    """
        function return a pandas dataFrame of shool grouped by 
        Ville column 
    """  
    data = df
    test = data.groupby(['Ville']).mean()
    print(test)
    return test
def runGroupSchoolMeanByTown():
    """
        function called by run.py (wrapper)
    """    
    groupSchoolMeanByTown(pd.read_csv(PATH_CSV_FILE_SCHOOL ,low_memory = False , sep=";" ))    
def groupSchoolMeanByTown(df) :
    """
        function return a pandas dataFrame grouped by 
        code commune
    """
    data = df
    test = data.groupby(['Code commune']).mean()
    print(test)
    
    return test
def runMergeSchoolAndCitiesByInsee():
    """
        function called by run.py (wrapper)
    """
    df1 = pd.read_csv(PATH_CSV_FILE_SCHOOL ,low_memory = False , sep=";" )
    df2 = pd.read_csv(PATH_CSV_FILE,low_memory = False , sep=";" )
    mergeSchoolAndCitiesByInsee([df1,df2])  
def mergeSchoolAndCitiesByInsee():
    """
        function return a merged pandas dataFrame  
        of cities.csv and schools.csv 
    """
    #get towns;
    cities_data = cities.read_cities_csv_data(settings.PATH_CSV_FILE)
    # les trier par population décroissante
    sorted_cities = cities.sort_cities_by_population(cities_data, '13') 
    # create graph
    bar_data = cities.create_graph(sorted_cities) 
    #show plot 
    # plot.show()
    #   
    # convert csv town to  dataframe
    sorted_cities = pd.DataFrame(sorted_cities) 
    #rename columns
    sorted_cities.rename(columns={'4':'Ville', '9':'Code commune', '13':'Population'}, inplace = True) 

    highschools_data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL) # récup csv lycées
    insee_averages = school.get_average(highschools_data)                                       
                                                   
    merge_result = pd.merge(insee_averages, sorted_cities[['Ville', 'Code commune', 'Population']], on='Code commune')
    sorted_by_population_results = cities.sort_cities_by_population(merge_result, 'Population')
    print(sorted_by_population_results)


    
    return sorted_by_population_results
'''

#-------------------------------------------------
def read_highschools_csv_data(path):
    data = pd.read_csv(path, low_memory=False, sep=";")
    #print(data.head().to_string())
    return data

def group_cities_districts(highschools):
    """
        function return a pandas dataFrame of distinct town
    """  
    return highschools.groupby(highschools['Ville'].str.startswith("PARIS")).mean()

def extract_highschools_columns(highschools):
    """
        function return a pandas dataFrame of shools by 
        code commune and Taux Brut
    """  
    highschools_df = pd.DataFrame(highschools) 
    return highschools_df.filter(items=['Code commune', 'Taux Brut de Réussite Total séries'])

def average_by_insee(highschools):
    print(highschools)
    data = highschools.groupby(['Code commune']).mean()
    #print(data)
    return data

def get_average(highschools):
    """
        function return la moyenne des notes par INNSEE
    """
    highschools_grouped_cities = group_cities_districts(highschools)
    highschools_extracted_columns = extract_highschools_columns(highschools_grouped_cities)
    return average_by_insee(highschools_extracted_columns)
#-------------------------------------------------

def update_field(col, data, criteria, updateValue):
    """
    col : column to patch 
    data : dataset
    criteria : array dep 
    updateValue :  
        """
    result = data.copy()
    
    result.update({col :    np.where (
            data[col].isin(criteria),
            updateValue,
            data[col]
        )})
    
    return result    



def borough_concatenation(data):

    dataW = regroupDistrict(data,'Code commune')
    result = dataW.groupby(['Code commune'] , as_index=False).agg({'Effectif de seconde' : 'sum'  })

    return result


def regroupDistrict (data,column_name) :

    for key , city in settings.CITIES.items() : 
       data = update_field(column_name, data, city['arr'], city['target']) 


    return data.groupby([column_name] , as_index=False).agg({'Effectif de seconde' : 'sum'  })        


def mergeDataframes (leftDF, rightDF, column_name) :
    return pd.merge(leftDF, rightDF, on=column_name)