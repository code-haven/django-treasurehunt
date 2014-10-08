from django.shortcuts import render
from django.http import HttpResponseRedirect
from treasurehunt.models import Level


def render_level(request, level):
	user = request.user.profile
	user_level = int(user.level)

	level_object = Level.objects.get(level=level)
	level = int(level)

	#Check if user has access to the current level
	if level <= user_level:
		if request.method == 'GET':
			return render(request, 'treasurehunt/level.html', {'level': level_object})

		elif request.method == 'POST':
			answer = str(level_object.answer).lower()
			user_answer = str(request.POST['answer']).lower()

			if answer == user_answer:
				#Update the level of user only if he is passing the level for first time
				if level == user_level:
					user.level += 1
					user.save(update_fields=['level'])
				else:
					pass
				return HttpResponseRedirect('/treasurehunt/level/%s' % str(int(level) + 1))

			else:
				return HttpResponseRedirect('/treasurehunt/level/%s' % level)
				
	#User does not have access
	else:
		return render(request, 'treasurehunt/no.html')

def index(request):
	render(request, 'index.html')