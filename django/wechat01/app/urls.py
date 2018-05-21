from django.conf.urls import patterns, url
from .views import verify

urlpatterns = patterns('',
                       url(r'^$', verify),
                       )