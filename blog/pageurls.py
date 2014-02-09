#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PageListView, PageDetailView, ReviewListView
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', PageListView.as_view(), name='list'),

    # redirect
    # url(r'^(?P<pk>\d+)/$', PageRedirectView.as_view(), name='detail'),

    url(r'^review/',ReviewListView.as_view(), name='review'),
    url(r'^massazh-v-moskve/', 'blog.views.vmoskve'),
    url(r'^massazh-na-domu/', 'blog.views.nadomu'),
    url(r'^manualnaya-terapiya/', 'blog.views.manual'),
    # url(r'^massazh-v-moskve/', VmoskveView.as_view(), name='vmoskve'),
    url(r'^(?P<slug>[-_\w]+)/$', PageDetailView.as_view(), name='detail'),
)
