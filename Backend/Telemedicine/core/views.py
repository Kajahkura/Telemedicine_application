from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def core(request):
    return HttpResponse("Service Coming soon...")
