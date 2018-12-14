from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from authorization.models import authorizationModel

# Create your views here.
def listone(request):
    try:
        user = authorizationModel.objects.get(name='jason')
    except Exception as e:
        errormessage = e
    return render(request, 'listone.html', locals())

def create_accont(request):
    if request.method == "POST":
        mess = request.POST['username']
    else:
        mess = "create fail"
    return render(request, 'create.html', locals())

def login(request):

    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('/login/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def authList(request):
    try:
        users = authorizationModel.objects.all().order_by('-id')

    except:
        error_message = "Get Users Error!"
    return render(request, "auth_users.html", locals())

def authDelete(request, pk=None):
    if request.method == 'GET':
        users = authorizationModel.objects.get(id=pk)
        return render(request, 'auth_delete.html', locals())

    elif request.method == 'POST':
        try:
            delete_account = authorizationModel.objects.get(id=pk)
            delete_account.delete()
            message = 'Delete success'

        except Exception as e:
            message = e
        return render(request, 'auth_result.html', locals())

def authUpdate(request, pk=None):
    if request.method == 'GET':
        users = authorizationModel.objects.get(id=pk)
        return render(request, 'auth_edit.html', locals())

    elif request.method == "POST":
        try:
            account = request.POST['account']
            password = request.POST['password']
            name = request.POST['name']
            line_id = request.POST['line_id']
            enable = request.POST['enable']

            update_account = authorizationModel.objects.get(id=pk)
            update_account.account = account
            update_account.password = password
            update_account.name = name
            update_account.line_id = line_id
            update_account.enable = enable
            update_account.save()

            message = 'update and save success'
        except Exception as e:
            message = e
        return render(request, 'auth_result.html', locals())

def authReg(request):
    if request.method == 'GET':
        return render(request, 'authReg.html')

    elif request.method == "POST":
        try:
            account = request.POST['account']
            password = request.POST['password']
            name = request.POST['name']
            line_id = request.POST['line_id']
            enable = request.POST['enable']

            add_account = authorizationModel.objects.create(account=account,password=password,name=name,line_id=line_id,enable=enable)
            add_account.save()
            message = 'create and save success'
        except Exception as e:
            message = e
        return render(request, 'auth_result.html', locals())
