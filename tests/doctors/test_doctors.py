from apps.school import school
from apps.cities import cities
from apps.utils import utils
from apps.doctors import doctors
import settings
import pandas as pd 

def test_countDoctor_field():
    data = doctors.read_doctors_csv_data(settings.PATH_CSV_FILE_DOCTORS)

    data = doctors.add_calculated_column(data)
    
    assert data.iloc[0]['countDoctor'] == 1

def test_borough_concatenation():

    data = doctors.read_doctors_csv_data(settings.PATH_CSV_FILE_DOCTORS)
    data = doctors.add_calculated_column(data)

    test  = doctors.borough_concatenation(data)

    # testCount = test.loc[test['c_depcom'] == "75056"]
    # print(testCount.iloc[0]['countDoctor'])
    
    assert   test.loc[test['city'] == "75056"].iloc[0]['countDoctor'] == 1498
    



