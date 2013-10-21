from django.conf.urls.defaults import *

urlpatterns = patterns('blog',
    url(r'^new/$', 'views.newArticle'),
)
