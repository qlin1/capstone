from django.conf.urls import url, include

import django.contrib.auth.views
from . import views

urlpatterns = [
	#test page
	url(r'^$', views.index, name = 'index'),
	url(r'^result$', views.result, name = 'result'),
	url(r'^comment/(?P<id>\d+)$', views.comment, name = 'comment'),
	# url(r'^final_result$', views.final_result, name = 'final_result'),
]

