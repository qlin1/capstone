from django.conf.urls import url, include

import django.contrib.auth.views
from . import views

urlpatterns = [
	#test page
	url(r'^$', views.login),
	url(r'^login$', views.login, name = 'login'),
	url(r'^index$', views.index, name = 'index'),
	url(r'^result$', views.result, name = 'result'),
	url(r'^dashboard$', views.dashboard, name = 'dashboard'),
	url(r'^comment/(?P<id>\d+)$', views.comment, name = 'comment'),
]

