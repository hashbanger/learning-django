from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat  for the entire month of January!",
    "february": "Walk for at least 20 minutes every day in February!",
    "march": "Learn Django for at least 20 minutes every day for the month of March!",
    "april": "Eat no meat for the entire month of April!",
    "may": "Walk for at least 20 minutes every day in May!",
    "june": "Learn Django for at least 20 minutes every day for the month of June!",
    "july": "Eat no meat for the entire month of July!",
    "august": "Walk for at least 20 minutes every day in August!",
    "september": "Learn Django for at least 20 minutes every day for the month of September!",
    "october": "Eat no meat for the entire month of October!",
    "november": "Walk for at least 20 minutes every day in November!",
    "december": "Learn Django for at least 20 minutes every day for the month of December!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += (
            f"<li><a href='{month_path}'><h3>'{capitalized_month}'</h3></a></li>"
        )

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")

    redirect_month = months[month - 1]

    # builds /challenges/month
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
