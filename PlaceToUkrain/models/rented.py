from django.db import models
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.user import UkrUser

class Rented(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(UkrUser, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    offer = models.IntegerField()

    def __str__(self):
        return str(self.start_date) + " " + str(self.end_date)

    @staticmethod
    def get_all_rented():
        return Rented.objects.all()

    @staticmethod
    def get_rented_by_user(user):
        return Rented.objects.filter(user=user)

    @staticmethod
    def get_rented_by_house(house):
        return Rented.objects.filter(house=house)