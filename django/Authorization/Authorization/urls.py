from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Authorization.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', include('user.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
