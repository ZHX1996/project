from django.conf.urls import include, url
from django.contrib import admin
from Search import views as Search_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ProjectD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',Search_views.index,name = 'index'),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'E:/project/django/ProjectD/static'}),
    url(r'^admin/', include(admin.site.urls)),
]
