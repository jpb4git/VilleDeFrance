from apps.utils import utils
import settings 
from apps.cities import cities , controller as cityController
from apps.school import school , controller as schoolController
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
        cityController.import_csv_table()

    if args.action == "save_school":
        schoolController.import_school_csv_table()

    if args.action == "show_school":
        schoolController.read_data_from_table()
