from apps.school import school
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
def test_lyon_borough_concatenation():
    
   
    data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL)

    data.update({'Code commune' :    np.where (
        data['Code commune'].isin(settings.boroughLyon),
        '69123',
        data['Code commune']
    )})
    
    test = data.groupby(['Code commune'] , as_index=False).agg({'Effectif de seconde' : 'sum'  })

    assert  len(test.loc[test['Code commune'] == "69123" ]) == 1
    
    assert  len(test.loc[test['Code commune'] == "69386" ]) == 0
    
    
    
