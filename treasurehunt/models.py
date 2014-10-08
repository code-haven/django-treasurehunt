from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm


#User profile model for treasure hunt
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	level = models.IntegerField(default=1)

	def __unicode__(self):
		return self.user.username

#Function to create a user profile when a user is created.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

#Model for rendering each level
class Level(models.Model):
	level = models.IntegerField(blank=False)
	title = models.CharField(max_length=140, blank=True)
	image = models.ImageField(upload_to='levels', blank=False)
	answer = models.CharField(max_length=140, blank=False)

	def __unicode__(self):
		return 'Level: %s' % str(self.level)



			