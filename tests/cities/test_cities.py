from apps.cities import app as cities
from apps.utils import app as utils
import settings

def test_csv_loading():
    data = cities.read_cities_csv_data(settings.PATH_CSV_FILE)
    assert (data.iloc[0][2]) == "OZAN"
    assert len(data) == 36700

def test_sorting():
    data = cities.read_cities_csv_data(settings.PATH_CSV_FILE)
    sorted_cities = utils.sort_cities_by_field(data, '13')
    assert (sorted_cities.iloc[0][2]) == "PARIS"
