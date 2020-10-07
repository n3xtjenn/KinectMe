from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.Dash.as_view(), name='Dash'),
]
