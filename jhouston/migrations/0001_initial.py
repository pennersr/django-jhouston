# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ErrorReport'
        db.create_table('jhouston_errorreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reported_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('line_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('remote_addr', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('jhouston', ['ErrorReport'])


    def backwards(self, orm):
        
        # Deleting model 'ErrorReport'
        db.delete_table('jhouston_errorreport')


    models = {
        'jhouston.errorreport': {
            'Meta': {'object_name': 'ErrorReport'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'reported_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['jhouston']
