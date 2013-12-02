#coding: utf-8
from django.conf.urls import patterns, url
from specialist.views import ExpertListView, ExpertDetailView
# from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    # (r'^$', ListView.object_list, all_models_dict),
    url(r'^$', ExpertListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ExpertDetailView.as_view(), name='detail'),
)
