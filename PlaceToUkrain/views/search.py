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

            if start_date is not None or end_date is not None:
                available_houses = []
                for house in houses:
                    house_periods = Period.get_periods_by_house(house)
                    if not Period.is_house_booked(house_periods, start_date, end_date):
                        available_houses.append(house)
                houses = available_houses

            return render(request, self.template_name, {'form': form, 'houses': houses})

        return render(request, self.template_name, {'form': form})
