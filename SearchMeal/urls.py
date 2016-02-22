from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from SearchMeal import views

urlpatterns = patterns('',
                       # url(r'^api/$', views.ViewsList.as_view()),
                       url(r'^api/(?P<pk>[0-9]+)$', views.ViewsList.as_view()),
                       url(r'^api/variations/(?P<var>.+)/$', views.VariationsList.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
