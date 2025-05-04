from django.db import models

class Speakers(models.Model):
    speaker_id = models.BigAutoField(primary_key=True)
    speaker_name = models.CharField(max_length=120)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'speakers'
