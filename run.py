from settings import PATH_CSV_FILE
import pandas as pd 


def load_plot(path) :
    
    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(path , names = ['A'  + str(i) for i in range(26)])  
    print(data)
   
    '''
    print(data['A5'])
    print(data['A14'])
    x = data['A5']
    y = data['A14']
    plt.scatter(x, y)
    plt.show()
    '''

if __name__ == '__main__':
   
    load_plot(PATH_CSV_FILE)