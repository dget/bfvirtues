# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Day'
        db.create_table(u'app_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='days', to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('temperance', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('silence', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('resolution', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('frugality', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('industry', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('sincerity', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('justice', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('moderation', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('cleanliness', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('tranquillity', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('chastity', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('humility', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal(u'app', ['Day'])


    def backwards(self, orm):
        
        # Deleting model 'Day'
        db.delete_table(u'app_day')


    models = {
        u'app.day': {
            'Meta': {'object_name': 'Day'},
            'chastity': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'cleanliness': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'frugality': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'humility': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'justice': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'moderation': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'resolution': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'silence': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'sincerity': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'temperance': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'tranquillity': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'days'", 'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 7, 19, 30, 58, 343543, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 7, 19, 30, 58, 342910, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']
