from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no mean for the entire month of January!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day in February!")
