from django.conf.urls import patterns, url

urlpatterns = patterns('investigations.views',
    url(r'^$', 'index', {'template_name':'investigations/index.html'}, name='index'),
)

