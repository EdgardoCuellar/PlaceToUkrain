from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from PlaceToUkrain.models.user import UkrUser
from django.views import View
from PlaceToUkrain.models.forms import LoginForm


class LoginView(View):
    return_url = None

    def get(self, request):
        LoginView.return_url = request.GET.get ('return_url')
        form = LoginForm ()
        return render (request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        error_message = 'Veuillez saisir vos informations de connexion'
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UkrUser.get_user_by_email (email)

            if user:
                flag = check_password (password, user.password)
                if flag:
                    request.session['user'] = user.id
                    
                    if LoginView.return_url:
                        return HttpResponseRedirect (LoginView.return_url)
                    else:
                        LoginView.return_url = None
                        return redirect ('index')
                else:
                    error_message = 'Mot de passe invalide !'
            else:
                error_message = 'Votre email n\'est pas enregistré !'
        return render (request, 'login.html', {'form': form, 'error': error_message})

def logout(request):
    request.session.clear()
    form = LoginForm ()
    return render (request, 'login.html', {'form': form})
