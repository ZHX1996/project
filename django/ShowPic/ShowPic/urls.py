from django.conf.urls import include, url
from django.contrib import admin
from MyApp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ShowPic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'D:/eclipse workspace/ShowPic/static'}),
    url(r'^admin/', include(admin.site.urls)),
]
