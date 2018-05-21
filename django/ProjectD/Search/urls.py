from django.conf.urls import patterns, url
from Search import views as Search_views
 
urlpatterns = patterns('',
         url(r'^$',Search_views.index, name = 'index'),
         url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'E:/project/django/ProjectD/static'}),
         )  
		 