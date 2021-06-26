from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sendMail(request):
    return HttpResponse('Sending email')

def sendEmail(request):
    print("I am sending email")
    return HttpResponse()