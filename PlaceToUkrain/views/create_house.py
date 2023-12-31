from django.shortcuts import render, redirect
from django.views import View
from django.forms.formsets import formset_factory
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.forms import HouseForm, PeriodForm
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.rented import Rented
from PlaceToUkrain.models.period import Period
import datetime

NB_MAX_PERIODS = 3

class CreateHouseView(View):

    def get(self, request):
        if not request.session.get('user'):
            return redirect('login')

        user = UkrUser.get_user_by_id(request.session.get('user'))

        if not user.is_host:
            return redirect('homepage')

        house_form = HouseForm()
        PeriodFormSet = formset_factory(PeriodForm, extra=NB_MAX_PERIODS)
        period_formset = PeriodFormSet(prefix='periods')  # Set a prefix for the formset

        return render(request, 'create_house.html', {'house_form': house_form, 'period_formset': period_formset})

    def post(self, request):
        house_form = HouseForm(request.POST)
        PeriodFormSet = formset_factory(PeriodForm, extra=NB_MAX_PERIODS)
        period_formset = PeriodFormSet(request.POST, prefix='periods')  # Set the same prefix used in the template

        if house_form.is_valid() and period_formset.is_valid():
            house = house_form.save(commit=False)
            house.user_id = request.session.get('user')
            house.save()

            bad_periods = 0
            current_period = None
            for period_form in period_formset:
                if not period_form.cleaned_data:
                    bad_periods += 1
                    continue
                else:
                    if Period.validate_dict_period(period_form.cleaned_data) is False:
                        bad_periods += 1
                        continue
                    if current_period is None:
                        period = period_form.save(commit=False)
                        current_period = period
                    else:
                        if Period.validate_two_periods_dict(current_period, period_form.cleaned_data) is False:
                            bad_periods += 1
                            continue
                        else:
                            period = period_form.save(commit=False)
                period.house = house 
                period.save()

            if bad_periods == NB_MAX_PERIODS:
                house.delete()
                return render(request, 'create_house.html', {'house_form': house_form, 'period_formset': period_formset, 'error': 'Il faut au moins une période de temps.'})

            return redirect('index')
        return render(request, 'create_house.html', {'house_form': house_form, 'period_formset': period_formset})

def delete_house(request, house_id):
    house = House.get_house_by_id(house_id)
    house.delete()
    return redirect('index')

def rent_house(request, house_id):
    period_str = request.POST.get('house_period')
    offer = request.POST.get('offer')
    rented = Rented()
    if offer is not None:
        rented.offer = offer
    rented.house_id = house_id
    rented.user_id = request.session.get('user')

    period = period_str.split(' au ')
    
    rented.start_date = datetime.datetime.strptime(period[0], '%Y-%m-%d').date()
    rented.end_date = datetime.datetime.strptime(period[1], '%Y-%m-%d').date()

    rented.save()

    return redirect('index')

def delete_rent(request, rented_id):
    rented = Rented.get_rented_by_id(rented_id)
    rented.delete()
    return redirect('index')