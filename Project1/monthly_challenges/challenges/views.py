from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
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
    "december": "dec challenge",
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