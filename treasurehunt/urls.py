from django.conf.urls import patterns, url
import treasurehunt.views

urlpatterns = patterns('', 
    url(r'^$', treasurehunt.views.index),

    url(r'^level/(?P<level>\d+)$', treasurehunt.views.render_level),
)
