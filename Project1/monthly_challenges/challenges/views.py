from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
monthly_challenges = {
    "january": "jan challenge",
    "february": "jan challenge",
    "march": "jan challenge",
    "april": "jan challenge",
    "may": "jan challenge",
    "june": "jan challenge",
    "july": "jan challenge",
    "august": "jan challenge",
    "september": "jan challenge",
    "october": "jan challenge",
    "november": "jan challenge",
    "december": "jan challenge",
}
def monthly_challenge(request,month):

    try:
        monthly_challenge_text = monthly_challenges[month]
        return HttpResponse(monthly_challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):

    try:
        if month > len(monthly_challenges):
            return HttpResponseNotFound("This Month is invalid")
        monthes = monthly_challenges.keys()
        print(monthes[0])
        retrun = HttpResponseRedirect("/challanges/"+monthes[month-1])

        return HttpResponse("test")
    except Exception as e:
        print(e)
        return HttpResponseNotFound("This month is not supported")