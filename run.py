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
  
    sorted_cities = pds.DataFrame(sorted_cities) # convertir villes en dataframe
    sorted_cities.rename(columns={'4':'Ville', '9':'Code commune', '13':'Population'}, inplace = True) # renommer colonnes

    highschools_data = highschools.read_highschools_csv_data(settings.highschools_csv_path) # récup csv lycées
    insee_averages = highschools.get_average(highschools_data)                                       
                                                   
    merge_result = pds.merge(insee_averages, sorted_cities[['Ville', 'Code commune', 'Population']], on='Code commune')
    sorted_by_population_results = cities.sort_cities_by_population(merge_result, 'Population')
    print(sorted_by_population_results)
