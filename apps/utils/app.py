

def renameColDataframe (data, columns_map) :
    return data.rename(columns=columns_map, inplace = False) # rename columns


def sort_cities_by_field(data, column):
    return data.sort_values(by=column, ascending=False)

     