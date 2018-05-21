from django.conf.urls import include, url
# from example.views import index, source, grass, factory, storage, logistic, sale, attention, ajax_dict
from example.views import index, ajax_dict

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^attention/$', attention, name='attention'),
    # url(r'^source/$', source, name='source'),
    # url(r'^grass/$', grass, name='grass'),
    # url(r'^factory/$', factory, name='factory'),
    # url(r'^storage/$', storage, name='storage'),
    # url(r'^logistic/$', logistic, name='logistic'),
    # url(r'^sale/$', sale, name='sale'),
    url(r'^ajax_dict/$', ajax_dict, name='ajax_dict'),
]

