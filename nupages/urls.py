from django.conf.urls import patterns, url

from .views import PageList, PageDetail



urlpatterns = patterns('nupages.views',
	url(r'^$', 'home_page', name='index'),
	# allows slugs to contain [_, -]
	#url(r'^(?P<slug>[-_\w]+)/$', PageDetail.as_view(), name='detail'),
	# allows anything to be a slug
	url(r'^(?P<slug>.*)/$', PageDetail.as_view(), name='detail'),
	url(r'^blog/$', PageList.as_view(), name='list'),
	
)