from django.shortcuts import render
from django.http import HttpResponse
from activity.models import classSummaryModel, signUpModel
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
	except:
		error_message = "Get Users Error!"
	return render(request, "users.html", locals())

def signUpList(request):
    try:
        users = signUpModel.objects.all().order_by('-id')
    except:
        error_message = "Get Users Error!"
    return render(request, "signup_users.html", locals())

def signUpDelete(request, pk=None):
    if request.method == 'GET':
        users = signUpModel.objects.get(id=pk)
        return render(request, 'delete.html', locals())

    elif request.method == 'POST':
        try:
            delete_account = signUpModel.objects.get(id=pk)
            delete_account.delete()
            message = 'Delete success'

        except Exception as e:
            message = e
        return render(request, 'signup_users.html', locals())

def signUpUpdate(request, pk=None):
    if request.method == 'GET':
        users = signUpModel.objects.get(id=pk)
        return render(request, 'signup_edit.html', locals())

    elif request.method == "POST":
        try:
            action_userID = request.POST['action_userID']
            action_classID = request.POST['action_classID']

            update_ID = signUpModel.objects.get(id=pk)
            update_ID.user_id = action_userID
            update_ID.class_id = action_classID

            update_ID.save()
            message = 'update and save success'
        except Exception as e:
            message = e
        return render(request, 'signup_result.html', locals())

def signUpReg(request):
    if request.method == 'GET':
        return render(request, 'signup_reg.html')

    elif request.method == "POST":
        try:
            action_userId = request.POST['action_userId']
            action_classId = request.POST['action_classId']
            time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_account = signUpModel.objects.create(user_id=action_userId,class_id=action_classId,signup_datetime=time)
            add_account.save()
            message = 'create and save success'
        except Exception as e:
            message = e
        return render(request, 'signup_result.html', locals())

def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')

    elif request.method == "POST":
        try:
            action_name = request.POST['action_name']
            action_detail = request.POST['action_detail']
            enable = request.POST['enable']

            time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_account = classSummaryModel.objects.create(action_name=action_name,action_detail=action_detail,action_datetime=time,enable=enable)
            add_account.save()
            message = 'create and save success'
        except Exception as e:
            message = e
        return render(request, 'result.html', locals())

def delete(request, pk=None):
    if request.method == 'GET':
        users = classSummaryModel.objects.get(id=pk)
        return render(request, 'delete.html', locals())

    elif request.method == 'POST':
        try:
            delete_account = classSummaryModel.objects.get(id=pk)
            delete_account.delete()
            message = 'Delete success'

        except Exception as e:
            message = e
        return render(request, 'result.html', locals())

def update(request, pk=None):
    if request.method == 'GET':
        users = classSummaryModel.objects.get(id=pk)
        action_name = users.action_name
        action_detail = users.action_detail

        return render(request, 'edit_user.html', locals())

    elif request.method == "POST":
        try:
            action_name = request.POST['action_name']
            action_detail = request.POST['action_detail']

            update_account = classSummaryModel.objects.get(id=pk)
            update_account.action_name = action_name
            update_account.action_detail = action_detail

            update_account.save()
            message = 'update and save success'
        except Exception as e:
            message = e
        return render(request, 'result.html', locals())
