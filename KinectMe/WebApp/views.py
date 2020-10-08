from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

def homepage(request):
    return render(request, 'site/homepage.html')

class Dash(generic.ListView):
    model = Profile
    template_name = 'site/event_description.html'
    context='Profile'
