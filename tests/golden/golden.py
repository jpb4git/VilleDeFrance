from settings import PATH_CSV_FILE
from run import load_plot
import pandas as pd 


def golden_master_state() :
    
    golden_data =  load_plot(PATH_CSV_FILE)
    #golden_data = golden_data.to_string()
    f= open("goldenpanda.txt","w+")
    f.write(golden_data.head(10).to_string())
    f.close
    
if __name__ == '__main__':
    golden_master_state    