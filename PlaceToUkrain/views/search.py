from django.shortcuts import render
from django.views import View
from django.db.models import Q
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.period import Period
from PlaceToUkrain.models.forms import HouseSearchForm
import math

class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        form = HouseSearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HouseSearchForm(request.POST)
        if form.is_valid():
            max_price = form.cleaned_data.get('max_price') 
            start_date = form.cleaned_data.get('period_start_date')
            end_date = form.cleaned_data.get('period_end_date')
            num_people = form.cleaned_data.get('num_people')  
            country = form.cleaned_data.get('country')
            city = form.cleaned_data.get('city')

            filters = Q()
            if max_price:
                filters = Q(price_type='gratuit') | Q(price__lte=max_price)
            if num_people:
                filters &= Q(people__gte=num_people)
            if country:
                filters &= Q(country__icontains=country)
            if city:
                filters &= Q(city__icontains=city)

            houses = House.objects.filter(filters)
            available_houses = self.get_availble_houses(houses, start_date, end_date)
            
            if len(available_houses) > 0:
                period = None
                if start_date is not None and end_date is not None:
                    period = str(start_date) + " au " + str(end_date)
                return render(request, self.template_name, {'form': form, 'houses': available_houses, 'period': period})
                
            propositions = self.create_proposition(houses, start_date, end_date, city)
            return render(request, self.template_name, {'form': form, 'houses': None, 'propositions': propositions})
            

        return render(request, self.template_name, {'form': form})

    def get_availble_houses(self, houses, start_date, end_date):
        available_houses = []
        if start_date is not None or end_date is not None:
            for house in houses:
                house_periods = Period.get_periods_by_house_available(house)
                
                for period in house_periods:
                    if start_date is not None and end_date is not None:
                        if period.start_date <= start_date and period.end_date >= end_date:
                            available_houses.append((house, period))
                    elif start_date is not None:
                        if period.start_date <= start_date and period.end_date >= start_date:
                            print(period.start_date, period.end_date)
                            available_houses.append((house, period))
                    elif end_date is not None:
                        if period.end_date >= end_date and period.start_date <= end_date:
                            available_houses.append((house, period))
        else:
            for house in houses:
                for period in Period.get_periods_by_house_available(house):
                    available_houses.append((house, period))
        return available_houses

    def create_proposition(self, houses, start_date, end_date, city=None):
        propositions = []

        if not city:
            for city in House.get_all_cities():
                houses_in_city = House.get_houses_by_city(city)
                propositions += self.create_proposition(houses_in_city, start_date, end_date, city)
            return propositions

        houses = House.get_houses_by_city(city)
        
        house_period = []
        for house in houses:
            periods = Period.get_periods_by_house_available(house)
            for period in periods:
                house_period.append((house, period))

        sorted_houses = sorted(house_period, key=lambda house_period: house_period[1].start_date)

        current_proposition = []

        current_date = start_date
        for house, period in sorted_houses:
            if period.start_date <= current_date and start_date <= period.end_date:
                if period.end_date <= end_date:
                    current_proposition.append((house, self.format_dates(current_date, period.end_date)))
                    current_date = period.end_date
                else:
                    current_proposition.append((house, self.format_dates(current_date, end_date)))
                    break
        propositions.append((current_proposition))
        return propositions

    def format_dates(self, start_date, end_date):
        return str(start_date) + " au " + str(end_date)
