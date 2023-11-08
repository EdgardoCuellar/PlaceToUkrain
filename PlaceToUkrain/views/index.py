from django.shortcuts import render, redirect
from django.views import View
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.house import House

class IndexView(View):

    def get(self, request):
        if not request.session.get('user'):
            return redirect('login')           
        user = UkrUser.get_user_by_id(request.session.get('user'))
        houses = House.get_houses_by_user_id(request.session.get('user'))
        return render(request, 'index.html', {'user': user, 'houses': houses})
