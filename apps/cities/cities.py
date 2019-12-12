from settings import PATH_CSV_FILE
import pandas as pd 


def memo () :

    #dd = {'index' : [1,2,3] , 'villes' : ['Paris', 'Marseille', 'Chartres'],'Population' : [2,3,1]  }    
    #ddSolution = {'index' : [3,1,2], 'villes' : ['Chartres','Paris', 'Marseille'],'Population' : [1,2,3]  }    
    '''
    index = data.index
    columns = data.columns
    values = data.values
    '''
    #data_frames = pd.DataFrame(data=dd)
    #print(data_frames)
    
    #test2 = data.loc[data['A3'] == 'paris']
    ##print(test2.to_string())
    
    
    #print(data).sort_values("A4")
    #print(data.iloc[[4,13],[4,22]])
    #print(data.loc[[5,14]]) #tableau une dimension sur l'indice 5 (col 5)
    #print(columns)
    #print(values) 

    '''
    print(data['A5'])
    print(data['A14'])
    x = data['A5']
    y = data['A14']
    plt.scatter(x, y)
    plt.show()
    '''

def load_plot(path) :
    print('load_plot_cities')
    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(path ,low_memory = False , names = ['A'  + str(i) for i in range(26)])  
    #data = pd.read_csv(path ,low_memory =False)  
    test= data.sort_values(by=['A14'], ascending=False)
    
    return test.head(50)

def selectOneTownByName(data_towns, town_name) :
    ## transformer string en df   !! 
    print(data_towns)
    print("abc", data_towns['A4'] == town_name)
    return  data_towns.loc[data_towns['A4'] == town_name]
