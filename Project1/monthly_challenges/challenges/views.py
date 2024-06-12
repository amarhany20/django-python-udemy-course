# Import necessary modules from Django
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from urllib3 import request

# from django.template.loader import render_to_string

# Create your views here.

# Define a dictionary containing monthly challenges
monthly_challenges = {
    "january": "jan challenge",
    "february": "feb challenge",
    "march": "march challenge",
    "april": "apr challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "sept challenge",
    "october": "oct challenge",
    "november": "nov challenge",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge(request, month):
    """
    A view function to handle requests for monthly challenges by month name.

    Parameters:
        request (HttpRequest): The HTTP request object.
        month (str): The name of the month.

    Returns:
        HttpResponse: An HTTP response containing the monthly challenge text.
        HttpResponseNotFound: A 404 Not Found response if the month is not supported.
    """
    try:
        monthly_challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": monthly_challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    """
    A view function to handle requests for monthly challenges by month number.

    Parameters:
        request (HttpRequest): The HTTP request object.
        month (int): The number of the month (1-based index).

    Returns:
        HttpResponseRedirect: A redirect response to the monthly challenge by month name.
        HttpResponseNotFound: A 404 Not Found response if the month number is invalid.
    """
    try:
        if month > len(monthly_challenges):
            return HttpResponseNotFound("This Month is invalid")
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("monthly_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except Exception as e:
        return HttpResponseNotFound("This month is not supported - Error: " + str(e))
