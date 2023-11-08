from django import forms
from PlaceToUkrain.models.user import UkrUser
from PlaceToUkrain.models.house import House
from PlaceToUkrain.models.period import Period

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UkrUser
        fields = ('email', 'password', 'is_host')
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['country', 'city', 'price_type', 'price', 'people']

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
        }
