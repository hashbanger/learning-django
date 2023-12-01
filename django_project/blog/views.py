from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this function is going to take the traffic from the home page
def home(request):
    return HttpResponse("<h1>Welcome to the blog!</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")