#coding: utf-8
from django.conf.urls import patterns, include, url
from firstBlog.views import HomeListView
from blog.views import ReviewListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstBlog.views.home', name='home'),
    # url(r'^firstBlog/', include('firstBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^page/', include('blog.pageurls', namespace="page")),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^contact/', 'feedback.views.contact'),
    url(r'^thankyou.html', 'feedback.views.thankyou'),
    url(r'^thankyou2.html', 'blog.views.thankyou2'),
    url(r'^review/', ReviewListView.as_view(), name='review'),
    url(r'^add-review/', 'blog.views.addReview'),
)
