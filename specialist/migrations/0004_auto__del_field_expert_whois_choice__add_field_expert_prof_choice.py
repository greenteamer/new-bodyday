# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Expert.whois_choice'
        db.delete_column(u'specialist_expert', 'whois_choice')

        # Adding field 'Expert.prof_choice'
        db.add_column(u'specialist_expert', 'prof_choice',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Expert.whois_choice'
        db.add_column(u'specialist_expert', 'whois_choice',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Deleting field 'Expert.prof_choice'
        db.delete_column(u'specialist_expert', 'prof_choice')


    models = {
        u'specialist.expert': {
            'Meta': {'ordering': "['title']", 'object_name': 'Expert'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'prof_choice': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['specialist']