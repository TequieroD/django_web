from django.shortcuts import render
from django.http import HttpResponse
from activity.models import classSummaryModel
import random, datetime, requests,datetime

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

def list(request):
	try:
		users = classSummaryModel.objects.all().order_by('-id')
		print(users)
	except:
		error_message = "Get Users Error!"
		print(error_message)
	return render(request, "users.html", locals())


def registration(request):
    try:
        #check params
        account_name = request.GET.get('account_name')
        action_detail = request.GET.get('action_detail')
        if account_name in [None,''] or action_detail in [None,'']:
            message = 'Params invalid'
            return render(request, 'result.html', locals())

        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_account = classSummaryModel.objects.create(action_name=account_name,action_detail=action_detail,action_datetime=time,enable=True)
        add_account.save()
        message = 'create and save success'
    except Exception as e:
        message = e
    return render(request, 'result.html', locals())

def delete(request):
    try:
        account_name = request.GET.get('account_name')
        if account_name in [None,'']:
            message = 'Params invalid'
            return render(request, 'result.html', locals())

        delete_account = classSummaryModel.objects.get(account_name=account_name)
        delete_account.delete()
        message = 'Delete success'
    except Exception as e:
        message = e
    return render(request, 'result.html', locals())

def update(request):
    try:
        account_name = request.GET.get('account_name')
        action_detail = request.GET.get('action_detail')

        update_account = classSummaryModel.objects.get(name='jason')
        update_account.account_name = account_name
        update_account,account_name = action_detail
        update_account.save()
        message = 'update and save success'
    except Exception as e:
        message = e
    return render(request, 'result.html', locals())
