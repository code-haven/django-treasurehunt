from django.conf.urls import patterns, url
import treasurehunt.views

urlpatterns = patterns('', 
    url(r'^$', treasurehunt.views.index),

    url(r'^login/$', treasurehunt.views.user_login),
    url(r'^logout/$', treasurehunt.views.user_logout),
    #url(r'^login_success/$', treasurehunt.views.login_success),
    #url(r'^login_failure/$', treasurehunt.views.login_failure),

    url(r'^level/(?P<level>\d+)$', treasurehunt.views.render_level),
    #url(r'^level/verysmart$', treasurehunt.views.cheater),
    #url(r'^level/final$', treasurehunt.views.winner),
)
