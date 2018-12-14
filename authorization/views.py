from django.shortcuts import render
from . models import authorizationModel
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.contrib import auth
# Create your views here.
def greeting(request, name=None):
	return render(request, "greeting.html", {"name": name})

def grade(request):
	import random
	score = random.randint(0, 100)
	return render(request, "grade.html", {'score': int(score)})

def filter(request):
	# More information
	# https://docs.djangoproject.com/en/2.1/ref/templates/builtins/
	add_value=98
	add_value_str='Grade: '
	add_slashes="I'm: Denny"
	upper_str="abcdefg"
	remove_space="a b_c d_e f_g"
	return render(request, "filter.html", locals())

def list(request):
	try:
		users = authorizationModel.objects.all().order_by('-id')
		print(users)
	except:
		error_message = "Get Users Error!"
		print(error_message)

	return render(request, "users.html", locals())

class UserListView(ListView):
	model = authorizationModel
	template_name = 'users.html'


class UserShowView(DetailView):
    model = authorizationModel
    template_name = 'show_user.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
	model = authorizationModel
	template_name = 'new_user.html'
	fields = '__all__'

class UserUpdateView(UpdateView):
    model = authorizationModel
    template_name = 'edit_user.html'
    fields = ['account', 'password', 'name', 'line_id', 'enable']

class UserDeleteView(DeleteView):
    model = authorizationModel
    template_name = 'delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users')

def login(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			msg = "{name} are login.".format(name = request.user.username)
		else:
			msg = "You're not login."
		return render(request, "login.html", {"msg": msg})
	elif request.method == "POST":

		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/login_check')
		else:
			msg = "Login Failed."
			return render(request, "login.html", {"msg": msg})

def logout(request):
	if request.user.is_authenticated:
		msg = "{name} logout Successful.".format(name = request.user.username)
		auth.logout(request)
	else:
		msg = "You're not login"
	return render(request, "logout.html", {"msg": msg})
		
def loginCheck(request):
	if request.user.is_authenticated:
		msg = "{name} login Successful.".format(name = request.user.username)
	else:
		msg = "You're not login"
	return render(request, "check_login.html", {"msg": msg})