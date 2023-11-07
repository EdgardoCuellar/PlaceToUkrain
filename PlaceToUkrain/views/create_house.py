from django.shortcuts import render, redirect
from django.views import View
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.forms import HouseForm

class CreateHouseView(View):
    def get(self, request):
        if not request.session.get('user'):
            return redirect('login')       

        user = UkrUser.get_user_by_id(request.session.get('user'))

        if user.is_host == False:
            return redirect('homepage')

        form = HouseForm()
        
        return render(request, 'create_house.html', {'form': form})

    def post(self, request):
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create_house.html', {'form': form})
