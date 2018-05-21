from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'miniCMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'app.views.column_detail', name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', 'app.views.article_detail', name='article'),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )