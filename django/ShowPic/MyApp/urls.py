from django.conf.urls import patterns, url
from MyApp import views
 
urlpatterns = patterns('',
         url(r'^$', views.index, name='index'),
         url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'D:/eclipse workspace/ShowPic/static'}),
         )