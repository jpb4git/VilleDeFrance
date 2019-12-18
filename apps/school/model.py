from  connect.connect import db
from peewee import *
from apps.cities.model  import City

class School(Model):
    city = ForeignKeyField(City, related_name='fk_school')
    globalRating = DecimalField(null=True)
    successRate = DecimalField(null=True)
    mentionRate = DecimalField(null=True)
    
    class Meta:
        database = db
        db_table = 'schools'