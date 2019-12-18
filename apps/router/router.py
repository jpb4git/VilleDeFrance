from apps.utils import utils
import settings 
from apps.cities import cities , utils as cityUtils
from apps.school import school , utils as schoolUtils
from matplotlib import pyplot
from peewee import *
import argparse




def setRoute() : 

    parser = argparse.ArgumentParser()
   
   
    #parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        help="Choose an action to execute",
        nargs="?",
        choices=[
            "school",
            "db",
            "save_city",
            "show_city",
            "save_school",
            "show_school",
        ],
    )
    args = parser.parse_args()

    if args.action == "school":
        init()

    if args.action == "db":
       db_setting()
  
    if args.action == "save_city":
        cityUtils.import_csv_table()

    if args.action == "save_school":
        schoolUtils.import_school_csv_table()

    if args.action == "show_school":
        schoolUtils.read_data_from_table()
