from apps.school import app as school
from apps.cities import app as cities
from apps.utils import app as utils
from apps.doctors import app as doctors
import settings
import pandas as pd 

def test_countDoctor_field():
    data = doctors.read_doctors_csv_data(settings.PATH_CSV_FILE_DOCTORS)

    data = doctors.add_calculated_column(data, 'countDoctor')
    
    assert data.iloc[0]['countDoctor'] == 1

def test_borough_concatenation():

    data = doctors.read_doctors_csv_data(settings.PATH_CSV_FILE_DOCTORS)
    data = doctors.add_calculated_column(data, 'countDoctor')

    test  = doctors.borough_concatenation(data)

    # testCount = test.loc[test['c_depcom'] == "75056"]
    # print(testCount.iloc[0]['countDoctor'])
    
    assert   test.loc[test['city'] == "75056"].iloc[0]['countDoctor'] == 1498


def test_rate_calcutate_field():

    data = pd.DataFrame({  
                'population' : [100 , 50, 500], 
            'countDoctors' : [10 , 5 , 5 ]
            }, index=None)

    result  = doctors.add_calculated_rate_column(data, 'rate') 

    # print(result)

    assert result.iloc[0]['rate'] == 10.0
    assert result.iloc[1]['rate'] ==  10.0
    assert result.iloc[2]['rate'] ==  100.0

        


