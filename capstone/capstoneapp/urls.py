from django.conf.urls import url, include

import django.contrib.auth.views
from . import views

urlpatterns = [
	#test page
	url(r'^$', views.index, name = 'index'),
	url(r'^result$', views.result, name = 'result'),
]

