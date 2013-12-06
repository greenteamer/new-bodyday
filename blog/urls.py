#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PostListView, PostDetailView
# from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    # (r'^$', ListView.object_list, all_models_dict),
    url(r'^$', PostListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='detail'),
)
