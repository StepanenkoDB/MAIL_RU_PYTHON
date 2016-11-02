from django.conf.urls import url,include
from finance.views import index
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^charges/$', views.post_all, name='post_all'),
	url(r'^charges/new$', views.add_charge, name='add_charge'),
]