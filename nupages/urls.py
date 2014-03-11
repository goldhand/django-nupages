from django.conf.urls import patterns, url

from .views import PageList, PageDetail



urlpatterns = patterns('nupages.views',
                       url(r'^$', PageList.as_view(), name='list'),
                       url(r'^/(?P<slug>\d+)$', PageDetail.as_view(), name='detail'),
)