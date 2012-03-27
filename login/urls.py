from django.conf.urls import patterns, include, url

urlpatterns = patterns('login.views',
    url(r'^$', 'index'),
    url(r'^validate$', 'validate'),
)
