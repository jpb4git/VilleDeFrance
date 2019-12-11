#import settings
from settings import PATH_CSV_FILE
from run import load_plot
import pandas as pd 
from pandas.util.testing import assert_frame_equal

def test_loadData() :
    ##TODO
    # test if csv loaded well
    original = load_plot(PATH_CSV_FILE); 
    pandatest = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})  
    ##TODO
    # 
    assert_frame_equal(original,pandatest)
    