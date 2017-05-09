from django.conf.urls import url, include

import django.contrib.auth.views
from . import views

urlpatterns = [
	#test page
	url(r'^$', views.login),
	url(r'^login$', views.login, name = 'login'),
	url(r'^role$', views.role, name = 'role'),
	url(r'^tool$', views.tool, name = 'tool'),
	url(r'^tool2/(?P<id>\d+)$', views.tool2, name = 'tool2'),
	url(r'^index$', views.index, name = 'index'),
	url(r'^result/(?P<id>\d+)$', views.result, name = 'result'),
	url(r'^comment/(?P<id>\w+)$', views.comment, name = 'comment'),
	url(r'^dashboard/(?P<id>\d+)$', views.dashboard, name = 'dashboard'),
	url(r'^p_dashboard/(?P<id>\d+)$', views.p_dashboard, name = 'p_dashboard'),
	url(r'^final_result/(?P<id>\d+)$', views.final_result, name = 'final_result'),
	url(r'^d_final_result/(?P<id>\w+)$', views.d_final_result, name = 'd_final_result'),
	url(r'^p_final_result/(?P<id>\w+)$', views.p_final_result, name = 'p_final_result'),
]

