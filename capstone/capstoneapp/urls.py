from django.conf.urls import url, include

import django.contrib.auth.views
from . import views

urlpatterns = [
	#test page
	url(r'^$', views.login),
	url(r'^login$', views.login, name = 'login'),
	url(r'^role$', views.role, name = 'role'),
	url(r'^tool$', views.tool, name = 'tool'),
	url(r'^index$', views.index, name = 'index'),
	url(r'^result/(?P<id>\d+)$', views.result, name = 'result'),
	url(r'^comment/(?P<id>\w+)$', views.comment, name = 'comment'),
	url(r'^dashboard/(?P<id>\d+)$', views.dashboard, name = 'dashboard'),
	url(r'^p_final_result$', views.p_final_result, name = 'p_final_result'),
]

