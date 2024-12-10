from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


monthly_challenges = {
    "january": "January challenge",
    "february": "February challenge",
    "march": "March challenge",
    "april": "April challenge",
    "may": "May challenge",
    "june": "June challenge",
    "july": "July challenge",
    "august": "August challenge",
    "september": "September challenge",
    "october": "October challenge",
    "november": "November challenge",
    "december": "December challenge"
}
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
