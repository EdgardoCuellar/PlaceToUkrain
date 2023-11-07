from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from PlaceToUkrain.models.forms import RegistrationForm
from PlaceToUkrain.models.user import UkrUser

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password = make_password (password)
            is_host = form.cleaned_data['is_host']

            user = UkrUser(email=email, password=password, is_host=is_host)

            user.save()
            
            return redirect('login')
            
        error = 'Authentication failed'
        return render(request, 'register.html', {'form': form, 'error': error})
