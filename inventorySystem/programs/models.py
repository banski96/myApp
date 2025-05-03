from django.db import models

class Programs(models.Model):
    program_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = 'programs'
