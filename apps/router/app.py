from apps.utils import app as utils
import settings 
from apps.cities import app as cities , controller as cityController
from apps.school import app as school , controller as schoolController
from apps.doctors import app as doctors , controller as doctorController
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
            "save_doctor",
            "show_doctor",

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

    if args.action == "save_doctor":
        doctorController.import_doctors_csv_table()

    if args.action == "show_doctor":
        doctorController.read_data_from_table()
