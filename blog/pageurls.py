#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PageListView, PageDetailView, ReviewListView
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', PageListView.as_view(), name='list'),

    # redirect
    # url(r'^(?P<pk>\d+)/$', PageRedirectView.as_view(), name='detail'),

    url(r'^review/',ReviewListView.as_view(), name='review'),
    url(r'^(?P<slug>[-_\w]+)/$', PageDetailView.as_view(), name='detail'),
)
