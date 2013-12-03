#coding: utf-8
from django.conf.urls import patterns, include, url
from firstBlog.views import HomeListView
from blog.views import ReviewListView
from django.views.generic import TemplateView

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from firstBlog.sitemaps import StaticViewSitemap
from blog.models import Post, Page

from django.contrib import admin
admin.autodiscover()


# for sitemap
info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'datetime',
}
info_dict2 = {
    'queryset': Page.objects.all(),
    'date_field': 'datetime',
}
sitemaps = {
    # 'flatpages': FlatPageSitemap,
    'static': StaticViewSitemap,
    'blog': GenericSitemap(info_dict, priority=0.6),
    'page': GenericSitemap(info_dict2, priority=0.7),
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstBlog.views.home', name='home'),
    # url(r'^firstBlog/', include('firstBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^experts/', include('specialist.urls', namespace="experts")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^page/', include('blog.pageurls', namespace="page")),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^contact/', 'feedback.views.contact'),
    url(r'^thankyou.html', 'feedback.views.thankyou'),
    url(r'^thankyou2.html', 'blog.views.thankyou2'),
    url(r'^review/', ReviewListView.as_view(), name='review'),
    url(r'^add-review/', 'blog.views.addReview'),

    #for seo
    url(r'^robots\.txt$', TemplateView.as_view(template_name='blog/robots.txt'), name="robots"),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
