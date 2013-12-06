# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('main_post_choice', self.gf('django.db.models.fields.CharField')(default='', max_length=7)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Page'
        db.create_table(u'blog_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('main_page_choice', self.gf('django.db.models.fields.CharField')(default='', max_length=7)),
        ))
        db.send_create_signal(u'blog', ['Page'])

        # Adding model 'Review'
        db.create_table(u'blog_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sender', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('review', self.gf('ckeditor.fields.RichTextField')()),
            ('review_choice', self.gf('django.db.models.fields.CharField')(default='', max_length=7)),
        ))
        db.send_create_signal(u'blog', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Page'
        db.delete_table(u'blog_page')

        # Deleting model 'Review'
        db.delete_table(u'blog_review')


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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.post': {
            'Meta': {'ordering': "['title']", 'object_name': 'Post'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main_post_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.review': {
            'Meta': {'ordering': "['title']", 'object_name': 'Review'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('ckeditor.fields.RichTextField', [], {}),
            'review_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']