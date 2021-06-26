from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="galleries"),
    path('getBaboons/', views.getBaboons, name="getBaboons")
]