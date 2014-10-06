from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from treasurehunt.models import Level
from django.core.context_processors import csrf


def render_level(request, level):
	user_level = request.user.profile.level

	if int(level) <= int(user_level):
		level_content = Level.objects.filter(level=level)
		return render(request, 'treasurehunt/level.html', )


def user_login(request):
	if request.method == 'GET':
		protected_form = {}
		form.update(csrf(request))

		return render(request, 'login.html', protected_form)

	elif request.method == 'POST':
		login_username = request.POST['username']
		login_password = request.POST['password']

		user = authenticate(username=login_username, password=login_password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/login_success/')
		else:
			return HttpResponseRedirect('/login_failure/')


def user_logout(request):
	user = request.user

	if user.is_authenticated():
		logout(request)
		return HttpResponseRedirect('/login/')