from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Profile

def homepage(request):
    return render(request, 'site/homepage.html')

#class Dash(generic.ListView):
    #model = Profile
   #template_name = 'site/dashboard.html'
    #context='Profile'