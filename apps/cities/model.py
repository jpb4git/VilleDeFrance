from  connect.connect import db
from peewee import *


class City(Model):
    insee = TextField(primary_key=True)
    name = TextField()
    population = IntegerField(null=True)
    longitude = DecimalField(null=True)
    latitude = DecimalField(null=True) 
    

    class Meta:

        database = db
        db_table = 'cities'
 