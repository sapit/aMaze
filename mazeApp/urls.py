from django.conf.urls import patterns, url
from mazeApp import  views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^challenge/$', views.challenge, name='challenge'),
            url(r'^solve/$', views.solve, name="solve"),
            url(r'^solve/(?P<maze_name>[\w\-]+)/$', views.solveMaze, name='solveMaze'),
        )