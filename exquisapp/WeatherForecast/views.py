from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def weatherInfo(request):
    return HttpResponse("I assist in getting the weather info")