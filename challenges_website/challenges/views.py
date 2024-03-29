from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Walk at least 20 minutes every day!",
    "may": "Walk at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Eat no meat for the entire month!",
    "september": "Eat no meat for the entire month!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Walk at least 20 minutes every day!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


    """ list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenge_path", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    # <li><a href="">January</a></li><li><a href="">February</a></li>...

    response_data = f
        <ul>
            {list_items}
        </ul>

    return HttpResponse(response_data) """


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    else:
        month_forwarded = months[month - 1]
        month_path = reverse("monthly_challenge_path", args=[month_forwarded])
        return HttpResponseRedirect(month_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })     
    except:
        raise Http404()
