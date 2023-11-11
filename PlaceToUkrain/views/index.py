from django.shortcuts import render, redirect
from django.views import View
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.rented import Rented

class IndexView(View):

    def get(self, request):
        if not request.session.get('user'):
            return redirect('login')           
            
        user = UkrUser.get_user_by_id(request.session.get('user'))

        if user.is_host:
            houses = House.get_houses_by_user_id(request.session.get('user'))

        else:
            rented = Rented.get_rented_by_user(user)
            houses = []
            for rent in rented:
                houses.append(rent.house)
        
        return render(request, 'index.html', {'user': user, 'houses': houses})
