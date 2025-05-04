from django.db import models

class Alumni(models.Model):
    alumni_id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=120)
    alumni_email = models.EmailField()
    mobile_number = models.CharField(max_length=16)
    graduation_year = models.DateField()
    degree = models.CharField(max_length=120)
    department = models.CharField(max_length=30)

    class Meta:
        db_table = 'alumni'
        