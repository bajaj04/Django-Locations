from django.conf.urls import patterns, include, url
from .views import locations,add_country_ajax,add_state_ajax,add_city_ajax,country_state_list_ajax,state_city_list_ajax
urlpatterns = patterns('',
    url(r'^location/$', locations, name='locations'),
    url(r'^add_country_ajax/$', add_country_ajax, name='add_country_ajax'),
    url(r'^add_state_ajax/$', add_state_ajax, name='add_state_ajax'),
    url(r'^add_city_ajax/$', add_city_ajax, name='add_city_ajax'),
    url(r'^country_state_list_ajax/$', country_state_list_ajax, name='country_state_list_ajax'),
    url(r'^state_city_list_ajax/$', state_city_list_ajax, name='state_city_list_ajax'),
)

