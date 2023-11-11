# views.py
from django.shortcuts import render
from django.views import View
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.rented import Rented

class StatisticsView(View):
    def get(self, request):
        countries = House.get_all_countries()

        country_statistics = []
        for country in countries:
            houses_offered = House.get_houses_by_country(country).count()
            
            rented_houses = Rented.get_all_rented()
            rented_houses_country = 0
            for rented_house in rented_houses:
                if rented_house.house.country == country:
                    rented_houses_country += 1

            country_statistics.append({
                'country': country,
                'houses_offered': houses_offered,
                'rented_houses_country': rented_houses_country,
            })

        context = {'country_statistics': country_statistics}
        return render(request, 'statistics.html', context)
