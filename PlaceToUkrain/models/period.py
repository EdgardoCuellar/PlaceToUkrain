from django.db import models
from PlaceToUkrain.models.house import House

class Period(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    renter = models.IntegerField()

    def __str__(self):
        return str(self.start_date) + " au " + str(self.end_date)

    @staticmethod
    def get_all_periods():
        return Period.objects.all()

    @staticmethod
    def get_periods_by_house(house):
        return Period.objects.filter(house=house)

    @staticmethod
    def get_periods_by_house_available(house):
        return Period.objects.filter(house=house, renter=None)