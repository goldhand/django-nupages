from django.conf.urls import patterns, url

from .views import PageList, PageDetail, PageFilter



urlpatterns = patterns('',
	url(r'^$', PageList.as_view(), name='list'),
	url(r'^filter/(?P<tag_slug>.*)/$', PageFilter.as_view(), name='filter'),
	# allows slugs to contain [_, -]
	#url(r'^(?P<slug>[-_\w]+)/$', PageDetail.as_view(), name='detail'),
	# allows anything to be a slug
	url(r'^(?P<slug>.*)/$', PageDetail.as_view(), name='detail'),
	
)