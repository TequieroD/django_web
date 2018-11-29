from django.shortcuts import render
from django.http import HttpResponse
from activity.models import classSummaryModel
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
