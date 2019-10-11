from django.conf.urls import url
from django.urls import include, path

from . import views


urlpatterns = [
	
	path('', views.index, name='index'),
	
]

#urlpatterns = [
#	path('', views.access, name='access'),
#]