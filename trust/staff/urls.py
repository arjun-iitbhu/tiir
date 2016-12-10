from django.conf.urls import patterns, url
from staff import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='page'))