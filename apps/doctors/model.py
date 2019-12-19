from  connect.connect import db
from peewee import *
from apps.cities.model  import City

class Doctor(Model):
    city = ForeignKeyField(City, related_name='fk_school')
    countDoctor = DecimalField(null=True)
    
    class Meta:
        database = db
        db_table = 'doctors'