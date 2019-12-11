from settings import PATH_CSV_FILE
import pandas as pd 
from apps.cities.cities import load_plot

'''
def load_plot(path) :
    
    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(path , names = ['A'  + str(i) for i in range(26)])  
    #print(data) 
   
    print(data['A5'])
    print(data['A14'])
    x = data['A5']
    y = data['A14']
    plt.scatter(x, y)
    plt.show()
   
    return data.head(10)
'''

def golden_master_state() :
    
    golden_data =  load_plot(PATH_CSV_FILE)
    #golden_data = golden_data.to_string()
    f= open("goldenpanda.txt","w+")
    f.write(golden_data.head(10).to_string())
    f.close



if __name__ == '__main__':
    #golden_master_state
    load_plot(PATH_CSV_FILE)