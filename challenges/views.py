from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

monthly_challenges = {
    "january": "Janus challenge",
    "february": "Februus challenge",
    "march": "Mars challenge",
    "april": "Aperire challenge",
    "may": "Maia challenge",
    "june": "Juno challenge",
    "july": "Julius challenge",
    "august": "Augustus challenge",
    "september": "September challenge",
    "october": "October challenge",
    "november": "November challenge",
    "december": None
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html",{
             "text": challenge_text, 
             "month_name": month
             })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
