from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from .models import ClubRules, ClubActivities, SpecialAnnounce, Suggestion, Complain, ClubInformation



# Create your views here.

# Index page
def index(request):
    return render(request,'index.html')

# member page
def member_panel(request):
    return render(request,'member.html')

# club rules page
def club_rules(request):
    rules = ClubRules.objects.all()
    rule_obj = rules[0]
    context = {"rule":rule_obj}
    return render(request,'clubrule.html',context)


def club_activities(request):
    activities = ClubActivities.objects.all()
    context = {"activities":activities}
    return render(request,'clubactivity.html',context)


def suggestion(request):
    success = False
    member_name = ""
    if request.method == "POST":
        member_name = request.POST["name"]
        member_email = request.POST["email"]
        member_suggestion = request.POST["suggestion"]
        suggestion_obj = Suggestion(member_name = member_name, member_email = member_email, member_suggestion=member_suggestion)
        suggestion_obj.save()
        success=True

    context = {"success":success, "member_name":member_name}

    return render(request,"suggestion.html", context)



def complain(request):
    success = False
    member_name = ""
    if request.method == "POST":
        member_name = request.POST["name"]
        member_email = request.POST["email"]
        member_complain = request.POST["complain"]
        complain_obj = Complain(member_name = member_name, member_email = member_email, member_complain=member_complain)
        complain_obj.save()
        success=True

    context = {"success":success, "member_name":member_name}

    return render(request,"complain.html", context)


def daily_activities(request):

    informations = ClubInformation.objects.all()
    context = {"informations":informations}
    return render(request,'daily-activities.html',context)

def specialAnnounce(request):

    announces = SpecialAnnounce.objects.all()
    context = {"announces":announces}
    return render(request,'specialanounce.html',context)