from django.db import models

class Period(models.Model):
    house_id = models.ForeignKey('House', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
