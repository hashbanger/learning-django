from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no mean for the entire month of January!",
    "february": "Walk for at least 20 minutes every day in February!",
    "march": "Learn Django for at least 20 minutes every day for the month of March!",
    "april": "Eat no mean for the entire month of April!",
    "may": "Walk for at least 20 minutes every day in May!",
    "june": "Learn Django for at least 20 minutes every day for the month of June!",
    "july": "Eat no mean for the entire month of July!",
    "august": "Walk for at least 20 minutes every day in August!",
    "september": "Learn Django for at least 20 minutes every day for the month of September!",
    "october": "Eat no mean for the entire month of October!",
    "november": "Walk for at least 20 minutes every day in November!",
    "december": "Learn Django for at least 20 minutes every day for the month of December!",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = monthly_challenges.keys()
    redirect_month = months[month]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
