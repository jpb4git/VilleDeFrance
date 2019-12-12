#import settings
from settings import PATH_CSV_FILE
from apps.cities.cities import load_plot,selectOneTownByName
import pandas as pd 
from pandas.util.testing import assert_frame_equal





def test_findTownByName() :
    df = create_dataframe_for_test()
    result =  selectOneTownByName( df, 'paris')
    assert result.iloc[0]['A4'] == 'paris'

# -- 
def create_dataframe_for_test():
    people_by_towns = [
                        ['Paris', 'paris', 100], 
                        ['Lyon', 'lyon', 200], 
                        ['Marseille', 'marseille', 400]
                      ]
    #rewrite the Columns name declared on the real dataset created before
    df = pd.DataFrame(people_by_towns, columns = ['A3', 'A4', 'A15']) 

    return df