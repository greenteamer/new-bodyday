#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PageListView, PageDetailView, ReviewListView

urlpatterns = patterns('',
    url(r'^$', PageListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', PageDetailView.as_view(), name='detail'),
    url(r'^review/',ReviewListView.as_view(), name='review'),
    url(r'^(?P<slug>[-_\w]+)/$', PageDetailView.as_view(), name='detail'),
)
