from django.shortcuts import render
from django.contrib.auth.models import user
from treasurehunt.models import Level


def render_level(request, level):
	user_level = request.user.profile.level

	if int(level) <= int(user_level):
		level_content = Level.objects.filter(level=level)
		return render(request, 'treasurehunt/level.html', )

