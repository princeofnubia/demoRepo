from django.urls import path # third party modules (a fra)
from . import views # import modules
urlpatterns = [ # list
    path('', views.weatherInfo, name="weatherinfo"), # function callin a list
    path('w/', views.weatherInfo, name="weatherinfo")
]
