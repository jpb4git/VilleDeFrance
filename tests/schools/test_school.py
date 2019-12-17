from apps.school import school
from apps.cities import cities
import settings
import pandas as pd 
import numpy as np 
'''
def test_csv_loading():
    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)
    assert (data['Etablissement'][0]) == "LYCEE PIERRE-GILLES DE GENNES"
    assert len(data) == 16210


def test_one_line_per_insee():
    data = {'Code commune': ['99999','99999','99999'], 'réussite' : [50.0, 75.0, 100.0]}
    df = pd.DataFrame(data)
    averages = school.average_by_insee(df)
    assert averages.iloc[0]['réussite'] == 75.0


def test_group_cities_districts():
    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)
    grouped_cities = school.group_cities_districts(data)
    assert len(grouped_cities) != 16210


def test_reduced_data_length():
    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)
    averages = school.get_average(data)
    assert len(averages) == 1157
'''
def test_borough_concatenation():
   
    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)

    test  = school.borough_concatenation(data)

    assert  len(test.loc[test['Code commune'] == "69123" ]) == 1
    assert  len(test.loc[test['Code commune'] == "69386" ]) == 0

    assert  len(test.loc[test['Code commune'] == "75056" ]) == 1
    assert  len(test.loc[test['Code commune'] == "75101" ]) == 0

    assert  len(test.loc[test['Code commune'] == "13055" ]) == 1
    assert  len(test.loc[test['Code commune'] == "13201" ]) == 0
    
def test_regroup_District():

    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)
    test  = school.regroupDistrict(data,'Code commune')

    assert  len(test.loc[test['Code commune'] == "69123" ]) == 1
    assert  len(test.loc[test['Code commune'] == "69386" ]) == 0

    assert  len(test.loc[test['Code commune'] == "75056" ]) == 1
    assert  len(test.loc[test['Code commune'] == "75857" ]) == 0

    assert  len(test.loc[test['Code commune'] == "13055" ]) == 1
    assert  len(test.loc[test['Code commune'] == "13556" ]) == 0
 
def test_mergeCitiesSchool():

    Rcities = cities.read_cities_csv_data(settings.PATH_CSV_FILE)
    Rcities.rename(columns={'4':'Ville', '9':'Code commune', '13':'Population'}, inplace = True) # renommer colonnes
    #print(Rcities['Code commune'])
    
    highschools_data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL) # récup csv lycées
    insee_averages_schools = school.regroupDistrict(highschools_data,'Code commune')                                       
    #print(insee_averages_schools['Code commune'])
   

    merge_result = school.mergeDataframes(insee_averages_schools, Rcities, 'Code commune')
    #print(merge_result['Ville'])
   
    
    sorted_by_population_results = cities.sort_cities_by_population(merge_result, 'Population')
    print(sorted_by_population_results['Ville'])

    assert  len(merge_result.loc[merge_result['Code commune'] == "75056" ]) == 1 
    assert  len(sorted_by_population_results.loc[sorted_by_population_results['Code commune'] == "75057" ]) == 0

# def test_mergeCitiesSchool():
 