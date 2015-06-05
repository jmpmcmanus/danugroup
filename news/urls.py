from django.conf.urls import patterns, include, url
from news.views import NewsSearch

urlpatterns = patterns('',
  url(r'^$', NewsSearch, name='danugroup_news_search'),
)

