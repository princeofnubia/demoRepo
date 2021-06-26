from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'gallery.html'
    context = {'my_name': "Oyewo"}
    return render(request, template, context)

def getBaboons(request):
    return HttpResponse('We are getting the baboons from the reserve')