from django.shortcuts import render, redirect
from django.views import View

class SearchView(View):
    def get(self, request):
        return render(request, 'search.html')
