#coding: utf-8
from django.contrib import admin
from gallery.models import Photo, PhotoAdmin

admin.site.register(Photo, PhotoAdmin)