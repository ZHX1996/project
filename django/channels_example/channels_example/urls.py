from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^', include('example.urls', namespace='example')),
    # url(r'^blog/', include('blog.urls')),
url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'E:/project/django/channels_example/static'}),
    url(r'^admin/', include(admin.site.urls)),
]
