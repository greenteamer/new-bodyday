# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table(u'mail_mail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'mail', ['Mail'])


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table(u'mail_mail')


    models = {
        u'mail.mail': {
            'Meta': {'ordering': "['title']", 'object_name': 'Mail'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mail']