from me_user.models import MeUser

from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, get_user_model

from django.http import HttpResponse

User = get_user_model()

# Create your views here.
def signup(request):
	if request.user.is_authenticated:
		return HttpResponse('Authenticated')

	username = request.POST.get('username')
	password = request.POST.get('password')

	if User.objects.filter(username = username).exists():
		return HttpResponse('User {} already exists'.format(username), status=400)

	user = MeUser.objects.create_user(username, password)
	auth_user = authenticate(username=username, password=password)
	return HttpResponse('Success')

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	auth_user = authenticate(username = username.lower(), password = password)
	if not auth_user:
		return HttpResponse('The user doesnt exist', status=400)
	else:
		auth_login(request, auth_user)
		return HttpResponse('Logged in')