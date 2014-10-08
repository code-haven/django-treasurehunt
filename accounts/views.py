from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect



def user_login(request):
	if request.method == 'GET':
		protected_form = {}
		protected_form.update(csrf(request))

		return render(request, 'accounts/login.html', protected_form)

	elif request.method == 'POST':
		login_username = request.POST['username']
		login_password = request.POST['password']

		user = authenticate(username=login_username, password=login_password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/accounts/login_success/')
		else:
			return HttpResponseRedirect('/accounts/login_failure/')


def user_logout(request):
	user = request.user

	if user.is_authenticated():
		logout(request)
		return HttpResponseRedirect('/accounts/login/')


def login_failure(request):
	return render(request, 'accounts/login_failure.html')

def login_success(request):
	return render(request, 'accounts/login_success.html')
