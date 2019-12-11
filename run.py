from settings import PATH_CSV_FILE
import pandas as pd 



def load_plot(path) :
    
    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(path , names = ['A'  + str(i) for i in range(26)])  
    
    #print(data) 
    '''
    print(data['A5'])
    print(data['A14'])
    x = data['A5']
    y = data['A14']
    plt.scatter(x, y)
    plt.show()
    '''
    return data

def golden_master_state() :
    
    golden_data =  load_plot(PATH_CSV_FILE)
    f= open("goldenpanda.txt","w+")
    f.write(str(golden_data.head(10)))
    f.close
    

if __name__ == '__main__':
    #golden_master_state()
    load_plot(PATH_CSV_FILE)