from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^home/$', 'permission.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'logout.html'}),
    url(r'^admin/', include(admin.site.urls)),
]
