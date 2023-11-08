"""
URL configuration for PlaceToUkrain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PlaceToUkrain.views.login import LoginView, logout
from PlaceToUkrain.views.register import RegistrationView
from PlaceToUkrain.views.homepage import HomepageView
from PlaceToUkrain.views.search import SearchView
from PlaceToUkrain.views.create_house import CreateHouseView, delete_house
from PlaceToUkrain.views.statistics import StatisticsView
from PlaceToUkrain.views.index import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout', logout , name='logout'),
    path('index/', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('create_house/', CreateHouseView.as_view(), name='create_house'),
    path('delete_house/<int:house_id>/', delete_house, name='delete_house'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]
