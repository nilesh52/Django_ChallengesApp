from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
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
    "december": None,
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{
            capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return render(request,"challenges/index.html",{
        "months":months
    })
    # return HttpResponse(response_data)

# def january(request):
#     return HttpResponse("This works!")


# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")


# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")
    redirect_month = months[month - 1]
    # /challenges/january
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
            })
        # response_date = f"<h1>{challenge_text}</h1>"
        # response_date = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_date)
    except:
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    # challenge_text = None
    # if month == 'january':
    #     challenge_text = "January Works!"
    # elif month == 'february':
    #     challenge_text = 'Walk for at least 20 minutes every day!'
    # elif month == 'march':
    #     challenge_text = 'Learn Django for at least 20 minutes every day!'
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
