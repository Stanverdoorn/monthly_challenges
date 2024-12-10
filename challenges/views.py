from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January challenge"
    elif month == "february":
        challenge_text = "February challenge"
    elif month == "march":
        challenge_text = "March challenge"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)