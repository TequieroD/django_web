from django.shortcuts import render
from authorization.models import authorizationModel

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