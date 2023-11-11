from django import template
from PlaceToUkrain.models.period import Period
from PlaceToUkrain.models.rented import Rented

register = template.Library()

@register.filter(name='get_periods')
def get_periods(house_id):
    periods = Period.get_periods_by_house(house_id)
    return periods

@register.filter(name='get_rented_periods')
def get_rented_periods(house_id, user_id):
    rented_periods = Rented.get_rented_by_house_and_user(house_id, user_id)   
    return rented_periods

@register.filter(name='datetime_list_to_str')
def datetime_list_to_str(datetimes):
    string = ""
    for datetime in datetimes:
        datetime = datetime.strftime("%Y-%m-%d")
        string += datetime + "\n"
    return string