from django.conf.urls import *

urlpatterns = patterns('contact.views',
  (r'^$', 'index', {'template_name':'contact/index.html'},'contact_index'),
  (r'^thankyou.html$', 'show_thankyou', {'template_name': 'contact/thankyou.html'}, 'contact_thankyou')
)

