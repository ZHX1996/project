from django.conf.urls import include, url
from django.contrib import admin
from myapp import views as myapp_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'oracle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',myapp_views.index,name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
]
