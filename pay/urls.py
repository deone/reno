from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pay.views', 
	url(r'^$', 'index', name='pay'),
    )
