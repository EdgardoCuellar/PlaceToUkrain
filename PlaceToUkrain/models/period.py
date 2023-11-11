from django.db import models
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.rented import Rented

class Period(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

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
        periods = Period.objects.filter(house=house)
        rented_periods = Rented.get_rented_by_house(house)

        avalaible_periods = []

        for period in periods:
            added = False
            for rented_period in rented_periods:
                if period.start_date <= rented_period.start_date and period.end_date >= rented_period.end_date:
                    if period.start_date < rented_period.start_date:
                        new_period.start_date = period.start_date
                        new_period.end_date = rented_period.start_date
                        new_period.house = house
                        avalaible_periods.append(new_period)
                    if period.end_date > rented_period.end_date:
                        new_period.start_date = rented_period.end_date
                        new_period.end_date = period.end_date
                        new_period.house = house
                        avalaible_periods.append(new_period)
                    added = True
                elif period.start_date <= rented_period.start_date and period.end_date <= rented_period.end_date:
                    new_period.start_date = period.start_date
                    new_period.end_date = rented_period.start_date
                    new_period.house = house
                    avalaible_periods.append(new_period)
                    added = True
                elif period.start_date >= rented_period.start_date and period.end_date >= rented_period.end_date:
                    new_period.start_date = rented_period.end_date
                    new_period.end_date = period.end_date
                    new_period.house = house
                    avalaible_periods.append(new_period)
                    added = True
            if added is False:
                avalaible_periods.append(period)   

        return avalaible_periods

    @staticmethod
    def validate_period(period):
        print(period)
        if period.start_date > period.end_date:
            return False
        return True

    @staticmethod
    def validate_dict_period(period):
        if period['start_date'] > period['end_date']:
            return False
        return True

    @staticmethod
    def validate_dates(start_date, end_date):
        if start_date > end_date:
            return False
        return True
    
    @staticmethod
    def validate_two_periods(period1, period2):
        if period1.start_date > period2.start_date:
            return False
        if period1.end_date > period2.start_date:
            return False
        return True

    @staticmethod
    def validate_two_periods_dict(period1, period2):
        if period1.start_date > period2['start_date']:
            return False
        if period1.end_date > period2['start_date']:
            return False
        return True
            

        