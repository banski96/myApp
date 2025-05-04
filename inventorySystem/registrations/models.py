from django.db import models
from alumni.models import Alumni
from events.models import Events

class Registrations(models.Model):
    registration_id = models.BigAutoField(primary_key=True)
    alumni_id = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    registration_date = models.DateField()
    status = models.CharField(max_length=25)

    class Meta:
            db_table = 'registrations'
