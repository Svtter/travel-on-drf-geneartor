# coding: utf-8

from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from api import views


urlpatterns = [

  url(r'^category/(?P<id>[0-9]+)$', views.CategoryAPIView.as_view()),
  url(r'^category/$', views.CategoryAPIListView.as_view()),

  url(r'^entry/(?P<id>[0-9]+)$', views.EntryAPIView.as_view()),
  url(r'^entry/$', views.EntryAPIListView.as_view()),

]
