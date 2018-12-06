from django.shortcuts import render, redirect
from django.http import HttpResponse
from activity.models import classSummaryModel, signUpModel
import random, datetime, requests

# Create your views here.
def info(request):
    number = random.randint(1,100)
    return render(request,"dice.html",{"info":number})
    #return HttpResponse("Hello Django!!")

def summary(request):
    name = 'Jason'
    number = random.randint(1,100)
    search_time = datetime.datetime.now()
    return render(request,"summary.html",{"name":name, "number":number, "search_time":search_time})

def list_activities(request):
    activities = classSummaryModel.objects.all().order_by('action_datetime')
    return render(request, "activities.html", {"activities": activities})

def show_activity(request, pk=None):
    activity = classSummaryModel.objects.get(id=pk)
    return render(request, "show_activity.html", {"activity": activity})

def create_activity(request, pk=None):
    if request.method == "GET":
        return render(request, "create_activity.html")

    elif request.method == "POST":
        action_name = request.POST['action_name']
        action_detail = request.POST['action_detail']
        action_datetime = request.POST['action_datetime']
        enable = True if request.POST['enable'] == 'on' else False
        activity = classSummaryModel.objects.create(action_name=action_name, action_detail=action_detail, action_datetime=action_datetime, enable=enable)
        activity.save()
        return redirect("/activities")

def update_activity(request, pk=None):
    if request.method == "GET":
        activity = classSummaryModel.objects.get(id=pk)
        return render(request, "update_activity.html", {"activity": activity})

    elif request.method == "POST":
        action_name = request.POST['action_name']
        action_detail = request.POST['action_detail']
        action_datetime = request.POST['action_datetime']
        enable = True if 'enable' in request.POST else False
        activity = classSummaryModel.objects.filter(id=pk).update(action_name=action_name, action_detail=action_detail, action_datetime=action_datetime, enable=enable)
        return redirect("/activities")

def delete_activity(request, pk=None):
    if request.method == "GET":
        activity = classSummaryModel.objects.get(id=pk)
        return render(request, "delete_activity.html", {"activity": activity})

    elif request.method == "POST":
        activity = classSummaryModel.objects.filter(id=pk)
        activity.delete()
        return redirect("/activities")