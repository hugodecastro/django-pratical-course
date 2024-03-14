from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
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
    list_items: str = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path: str = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"'>{capitalized_month}</a></li>"

    response_data: str = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)

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
        response_text: str = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": response_text
        })
    except:
        return HttpResponseNotFound(response_text)
