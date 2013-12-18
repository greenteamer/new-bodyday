# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mail.to'
        db.add_column(u'mail_mail', 'to',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mail.to'
        db.delete_column(u'mail_mail', 'to')


    models = {
        u'mail.mail': {
            'Meta': {'ordering': "['title']", 'object_name': 'Mail'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to': ('django.db.models.fields.EmailField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['mail']