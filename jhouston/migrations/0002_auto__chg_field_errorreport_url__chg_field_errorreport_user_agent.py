# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ErrorReport.url'
        db.alter_column('jhouston_errorreport', 'url', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ErrorReport.user_agent'
        db.alter_column('jhouston_errorreport', 'user_agent', self.gf('django.db.models.fields.TextField')())


    def backwards(self, orm):
        
        # Changing field 'ErrorReport.url'
        db.alter_column('jhouston_errorreport', 'url', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Changing field 'ErrorReport.user_agent'
        db.alter_column('jhouston_errorreport', 'user_agent', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'jhouston.errorreport': {
            'Meta': {'object_name': 'ErrorReport'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'reported_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {}),
            'user_agent': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['jhouston']
