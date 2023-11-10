from django.db import models
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.user import UkrUser

class Rented(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    user_id = models.ForeignKey(UkrUser, on_delete=models.CASCADE)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_date) + " " + str(self.end_date)

    @staticmethod
    def get_all_periods():
        return Period.objects.all()

    @staticmethod
    def get_periods_by_house(house):
        return Period.objects.filter(house=house)

    @staticmethod
    def get_periods_by_house_available(house):
        return Period.objects.filter(house=house, renter=None)