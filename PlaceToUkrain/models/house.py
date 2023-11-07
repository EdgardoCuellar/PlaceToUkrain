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

    