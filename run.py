from apps.router.app import setRoute


def init():
    '''
    Launcher app  

    '''
    fullCities = cities.read_cities_csv_data(settings.PATH_CSV_FILE)
    fullCities = utils.renameColDataframe(fullCities,{'4':'Ville', '9':'Code commune', '13':'Population'})
    selectionCities = fullCities[['Ville', 'Code commune', 'Population']]

    highschools_data = school.read_highschools_csv_data(settings.PATH_CSV_FILE_SCHOOL) 

    big_Cities = utils.sort_cities_by_field(selectionCities, 'Population').head(50)
    
    schoolByDistrict  = school.regroupDistrict(highschools_data,'Code commune')

    merge_result = school.mergeDataframes(schoolByDistrict, big_Cities, 'Code commune')

    result1  = school.add_calculated_column(merge_result)
    result = utils.sort_cities_by_field(result1, 'Score')
    result.head(100).plot.bar(x='Ville', y='Score', figsize=(12,12))
    
    print(result.head(50))

if __name__ == '__main__':
  
  setRoute()
  
