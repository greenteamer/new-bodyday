# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostGallery'
        db.create_table(u'blog_postgallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
        ))
        db.send_create_signal(u'blog', ['PostGallery'])


    def backwards(self, orm):
        # Deleting model 'PostGallery'
        db.delete_table(u'blog_postgallery')


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
        u'blog.postgallery': {
            'Meta': {'object_name': 'PostGallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"})
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