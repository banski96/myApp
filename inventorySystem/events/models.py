from django.db import models

class Events(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date =  models.DateField()
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

