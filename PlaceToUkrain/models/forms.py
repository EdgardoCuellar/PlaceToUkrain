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

class HouseSearchForm(forms.Form):
    max_price = forms.IntegerField(label='Maximum Price', required=False)
    period_start_date = forms.DateField(label='Period Start Date', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    period_end_date = forms.DateField(label='Period End Date', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    num_people = forms.IntegerField(label='Number of People', required=False)
    country = forms.CharField(label='Country', max_length=128, required=False)
    city = forms.CharField(label='City', max_length=128, required=False)

