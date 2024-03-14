from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges: dict[str, str] = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}


def index(request) -> HttpResponse:
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month) -> HttpResponse:
    months = list(monthly_challenges.keys())

    if month == 0 or month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str) -> HttpResponse:
    response_text: str = "<h1>This month is not supported!</h1>"
    try:
        response_text: str = monthly_challenges.get(month)
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": response_text
        })
    except ValueError:
        return HttpResponseNotFound(response_text)
