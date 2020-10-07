from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class Dash(generic.ListView):
    model = Profile
    template_name = 'site/dashboard.html'
    context='Profile'
