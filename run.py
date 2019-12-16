from settings import PATH_CSV_FILE
from settings import PATH_CSV_FILE_SCHOOL
from apps.cities.cities import loadData
from apps.school.school import groupSchoolByInsee,groupSchoolMeanByTown,runGroupSchoolMeanByTown
'''
def golden_master_state() :
    
   # golden_data =  load_plot(PATH_CSV_FILE)
    #golden_data = golden_data.to_string()
    #f= open("goldenpanda.txt","w+")
    #f.write(golden_data.head(10).to_string())
    #f.close
    
    print('entering statement')
    golden_data =  load_plot(PATH_CSV_FILE)
    golden_data = golden_data.to_string()
    f= open("goldenData.txt","w+")
    f.write(golden_data)
    f.close
'''    


if __name__ == '__main__':
    #golden_master_state()
    loadData(PATH_CSV_FILE)
    #selectOneTownByName('paris')
    #runGroupSchoolMeanByTown() 
