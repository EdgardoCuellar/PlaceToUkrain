from django.shortcuts import render, redirect
from django.views import View
from django.forms.formsets import formset_factory
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.forms import HouseForm, PeriodForm
from PlaceToUkrain.models.house import House

class CreateHouseView(View):
    def get(self, request):
        if not request.session.get('user'):
            return redirect('login')

        user = UkrUser.get_user_by_id(request.session.get('user'))

        if not user.is_host:
            return redirect('homepage')

        house_form = HouseForm()
        PeriodFormSet = formset_factory(PeriodForm)
        period_formset = PeriodFormSet(prefix='periods')  # Set a prefix for the formset

        return render(request, 'create_house.html', {'house_form': house_form, 'period_formset': period_formset})

    def post(self, request):
        house_form = HouseForm(request.POST)
        PeriodFormSet = formset_factory(PeriodForm)
        period_formset = PeriodFormSet(request.POST, prefix='periods')  # Set the same prefix used in the template

        print(len(period_formset))
        for period_form in period_formset:
            print(period_form)

        if house_form.is_valid() and period_formset.is_valid():
            house = house_form.save(commit=False)
            house.user_id = request.session.get('user')
            house.save()

            # Process and associate periods with the house
            for period_form in period_formset:
                if not period_form.cleaned_data:
                    continue

                period = period_form.save(commit=False)
                period.house = house 
                period.save()

            return redirect('index')
        return render(request, 'create_house.html', {'house_form': house_form, 'period_formset': period_formset})

def delete_house(request, house_id):
    house = House.get_house_by_id(house_id)
    house.delete()
    return redirect('index')
