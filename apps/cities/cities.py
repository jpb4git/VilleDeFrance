from settings import PATH_CSV_FILE
import pandas as pd 


def load_plot(path) :
    
    # Load the Pandas libraries with alias 'pd' 
    data = pd.read_csv(path , names = ['A'  + str(i) for i in range(26)])  
    index = data.index
    columns = data.columns
    values = data.values
    dd = {'index' : [1,2,3] , 'villes' : ['Paris', 'Marseille', 'Chartres'],'Population' : [2,3,1]  }    
    ddSolution = {'index' : [3,1,2], 'villes' : ['Chartres','Paris', 'Marseille'],'Population' : [1,2,3]  }    
    
    data_frames = pd.DataFrame(data=dd)
    print(data_frames)

    #print(data[['A4',"A15","A16","A17"]]).sort_values("A4", ascending=False)
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
    return data.head(10)