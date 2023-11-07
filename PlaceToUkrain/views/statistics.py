from django.shortcuts import render, redirect
from django.views import View

class StatisticsView(View):
    def get(self, request):
        return render(request, 'statistics.html')
