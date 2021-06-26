from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('getBaboons/', views.getBaboons, name="getBaboons"),
    path('sendEmail/', views.sendEmail, name="sendEmail")
]