from django.conf.urls import patterns, url

urlpatterns = patterns('investigations.ghgrp.views',
  url(r'^$', 'ghgrp', {'template_name': 'investigations/ghgrp/index.html'}, name='ghgrp'),
  url(r'^ghginvbar.html$', 'ghginvbar', {'template_name': 'investigations/ghgrp/ghginvbar.html'}),
  url(r'^ghgsectorgasemissions.html$', 'ghgsectorgasemissions', {'template_name': 'investigations/ghgrp/ghgsectorgasemissions.html'}),
  url(r'^ghgsectorgas.html$', 'ghgsectorgas', {'template_name': 'investigations/ghgrp/ghgsectorgas.html'}),
  url(r'^ghgmap.html$', 'ghgmap', {'template_name': 'investigations/ghgrp/ghgmap.html'}),
)
