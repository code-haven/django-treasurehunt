from django.conf.urls import patterns, url
import accounts.views


urlpatterns = patterns('', 
    url(r'^login/$', accounts.views.user_login),
    url(r'^logout/$', accounts.views.user_logout),
    url(r'^login_success/$', accounts.views.login_success),
    url(r'^login_failure/$', accounts.views.login_failure),
)