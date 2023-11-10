from django import template
from PlaceToUkrain.models.period import Period

register = template.Library()

@register.filter(name='get_periods')
def get_periods(house_id):
    periods = Period.get_periods_by_house(house_id)
    periods_str = ""
    for period in periods:
        periods_str += str(period) + "\n"
    return periods_str

@register.filter(name='datetime_list_to_str')
def datetime_list_to_str(datetimes):
    string = ""
    for datetime in datetimes:
        datetime = datetime.strftime("%Y-%m-%d")
        string += datetime + "\n"
    return string