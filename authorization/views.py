from django.shortcuts import render
#from django.http import HttpResponse
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
