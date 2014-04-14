#coding: utf-8
from django.contrib import admin
from blog.models import *
from mail.models import Mail
from specialist.models import Expert

class PostGalleryAdmin(admin.StackedInline):
    model = PostGallery

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [PostGalleryAdmin,]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Expert)
admin.site.register(Post, PostAdmin)
admin.site.register(Page)
admin.site.register(Review)
admin.site.register(Mail)

