from django.db import models

PRICE_TYPE_CHOICES = [
    ('payant', 'Payant'),
    ('gratuit', 'Gratuit'),
    ('variable', 'Variable'),
]

class House(models.Model):
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    price_type = models.CharField(max_length=128, choices=PRICE_TYPE_CHOICES)
    price = models.IntegerField()
    people = models.IntegerField()
    user_id = models.IntegerField()
    
    def __str__(self):
        return self.country + " " + self.city + " " + self.price_type + " " + str(self.price) + " " + str(self.people)

    @staticmethod
    def get_all_houses():
        return House.objects.all()

    @staticmethod
    def get_houses_by_country(country):
        return House.objects.filter(country=country)
    
    @staticmethod
    def get_houses_by_city(city):
        return House.objects.filter(city=city)
        
    @staticmethod
    def get_houses_by_user_id(id):
        return House.objects.filter(user_id=id)

    @staticmethod
    def get_house_by_id(id):
        try:
            return House.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_houses_by_city(city):
        return House.objects.filter(city=city)

    @staticmethod
    def get_all_cities():
        return House.objects.values_list('city', flat=True).distinct()