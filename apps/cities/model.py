from  connect.connect import db
from peewee import *


class City(Model):
    insee = CharField(primary_key=True, max_length=6)
    name = CharField(max_length=75)
    population = IntegerField(null=True)
    longitude = DecimalField(null=True)
    latitude = DecimalField(null=True) 
    

    class Meta:

        database = db
        db_table = 'cities'
 