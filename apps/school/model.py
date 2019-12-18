class School(Model):
    insee = ForeignKeyField(towns, related_name='fk_school')
    name = TextField()
    globalRating : DecimalField()
    successRate : DecimalField()
    mentionRate : DecimalField()
    
    class Meta:
        database = db
        db_table = 'schools'