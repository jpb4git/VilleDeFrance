#import settings
from settings import PATH_CSV_FILE
from run import load_plot
import pandas as pd 
from pandas.util.testing import assert_frame_equal




def test_loadData() :
    ##TODO
    # test if csv loaded well
    workingData = load_plot(PATH_CSV_FILE); 
    
    f= open("goldenpanda.txt","r")
    goldenData = f.read()
    f.close
    ##TODO
    # 
    assert goldenData == workingData.head(10).to_string()
    