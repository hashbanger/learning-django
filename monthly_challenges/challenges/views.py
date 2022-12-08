from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no mean for the entire month of January!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day in February!"
    elif month == "march":
        challenge_text = (
            "Learn Django for at least 20 minutes every day for the month of March!"
        )
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
