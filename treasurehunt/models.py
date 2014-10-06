from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	level = models.IntegerField(default=1)

	def __unicode__(self):
		return self.user.username


class Level(models.Model):
	level = models.IntegerField(blank=False)
	title = models.CharField(max_length=140, blank=True)
	image = models.ImageField(upload_to='levels', blank=False)
	answer = models.CharField(max_length=140, blank=False)

	def __unicode__(self):
		return str(self.level)
