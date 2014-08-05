from django.conf.urls import patterns, url

from shownotes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getContent/$', views.getContent, name='getContent'),
)