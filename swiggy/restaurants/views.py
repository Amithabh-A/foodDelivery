from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def restaurants(request):
    return HttpResponse("Hello world!")
