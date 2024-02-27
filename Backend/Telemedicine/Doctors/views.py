from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Health_practitioneer(request):
    message = 'Coming Soon....'
    return HttpResponse(message)
