from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges: dict[str, str] = {
    "january": "[Jan] Eat no meat for the entire month!",
    "february": "[Feb] Walk for at least 20 minutes every day!",
    "march": "[Mar] Learn Django for at least 20 minutes every day!",
    "april": "[Apr] Eat no meat for the entire month!",
    "may": "[May] Walk for at least 20 minutes every day!",
    "june": "[Jun] Learn Django for at least 20 minutes every day!",
    "july": "[Jul] Eat no meat for the entire month!",
    "august": "[Aug] Walk for at least 20 minutes every day!",
    "september": "[Sep] Learn Django for at least 20 minutes every day!",
    "october": "[Oct] Eat no meat for the entire month!",
    "november": "[Nov] Walk for at least 20 minutes every day!",
    "december": "[Dec] Learn Django for at least 20 minutes every day!"
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


def monthly_challenge(request, month) -> HttpResponse:
    response_text: str = "<h1>This month is not supported!</h1>"
    try:
        response_text: str = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(response_data)
