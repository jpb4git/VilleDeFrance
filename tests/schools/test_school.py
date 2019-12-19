from apps.school import school
from apps.cities import cities
from apps.utils import utils
import settings
import pandas as pd 

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
    col_map = {'4':'Ville', '9':'Code commune', '13':'Population'}
    Rcities = utils.renameColDataframe(Rcities, col_map)
    #print(Rcities['Code commune'])
    
    highschools_data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL) # récup csv lycées
    insee_averages_schools = school.regroupDistrict(highschools_data,'Code commune')                                       
    #print(insee_averages_schools['Code commune'])
   

    merge_result = school.mergeDataframes(insee_averages_schools, Rcities, 'Code commune')
    #print(merge_result['Ville'])
   
    
    sorted_by_population_results = utils.sort_cities_by_field(merge_result, 'Population')
    #print(sorted_by_population_results['Ville'])

    assert  len(merge_result.loc[merge_result['Code commune'] == "75056" ]) == 1 
    assert  len(sorted_by_population_results.loc[sorted_by_population_results['Code commune'] == "75057" ]) == 0

def test_add_calculated_column():
 
    data = pd.DataFrame({  
             'Taux Brut de Réussite Total séries' : [10.0 , 8.0, 10.0], 
            'Taux_Mention_brut_toutes_series' : [10.0 , 5.0 , 7.0 ]
            }, index=None)
    result  = school.add_calculated_column(data) 
    result = utils.sort_cities_by_field(result, 'Score')
   # print(result)
    
    assert result.iloc[0]['Score'] == 2.0
    assert result.iloc[1]['Score'] ==  1.7
    assert result.iloc[2]['Score'] ==  1.3

