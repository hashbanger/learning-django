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
    "december": None
    # "december": "Learn Django for at least 20 minutes every day for the month of December!",
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


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
        return render(
            request,
            "challenges/challenge.html",
            {"month_name": month, "text": challenge_text},
        )
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
