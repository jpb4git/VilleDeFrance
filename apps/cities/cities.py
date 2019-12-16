import pandas as pds
from pandas import DataFrame
import settings

def read_cities_csv_data(path):
    return pds.read_csv(path, low_memory=False, names=[str(i) for i in range(26)])

def sort_cities_by_population(data, column):
    return data.sort_values(by=column, ascending=False)

def create_graph(sorted_data):
    bar_data = DataFrame(sorted_data.head(settings.cities_max_number))
    return bar_data.plot(x=2, y=15, kind='bar')
