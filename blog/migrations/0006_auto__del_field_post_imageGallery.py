# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.imageGallery'
        db.delete_column(u'blog_post', 'imageGallery')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Post.imageGallery'
        raise RuntimeError("Cannot reverse this migration. 'Post.imageGallery' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Post.imageGallery'
        db.add_column(u'blog_post', 'imageGallery',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True),
                      keep_default=False)


    models = {
        u'blog.page': {
            'Meta': {'ordering': "['title']", 'object_name': 'Page'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'main_page_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.post': {
            'Meta': {'ordering': "['title']", 'object_name': 'Post'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'main_post_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.review': {
            'Meta': {'ordering': "['title']", 'object_name': 'Review'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'review_thumb/good.png'", 'max_length': '100'}),
            'review': ('ckeditor.fields.RichTextField', [], {}),
            'review_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']