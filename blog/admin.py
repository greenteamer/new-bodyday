#coding: utf-8
from django.contrib import admin
from blog.models import Post, Page, Review

admin.site.register(Post)
admin.site.register(Page)
admin.site.register(Review)

