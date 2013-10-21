from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^opportunities/', include('opportunity.urls')),
    url(r'^$', 'main.views.mainView', name='home'),
    url(r'^partners$', 'main.views.partnersView'),
    url(r'^accounts/register/', 'main.views.register'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^/accounts/profile/', 'main.views.userProfile'),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
