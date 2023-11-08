from django.db import models
from PlaceToUkrain.models.house import House

class Period(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.start_date) + " " + str(self.end_date)

    @staticmethod
    def get_all_periods():
        return Period.objects.all()

    @staticmethod
    def get_periods_by_house(house):
        return Period.objects.filter(house=house)