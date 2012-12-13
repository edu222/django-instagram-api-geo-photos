# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('core_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Tag'])

        # Adding model 'Location'
        db.create_table('core_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Location'])

        # Adding model 'Geography'
        db.create_table('core_geography', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('distance', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Geography'])

        # Adding model 'Map'
        db.create_table('core_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_geography', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Geography'])),
        ))
        db.send_create_signal('core', ['Map'])

        # Adding model 'User'
        db.create_table('core_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['User'])

        # Adding model 'Place'
        db.create_table('core_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_geography', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Geography'], blank=True)),
            ('a_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Location'], blank=True)),
            ('a_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Tag'], blank=True)),
        ))
        db.send_create_signal('core', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('core_tag')

        # Deleting model 'Location'
        db.delete_table('core_location')

        # Deleting model 'Geography'
        db.delete_table('core_geography')

        # Deleting model 'Map'
        db.delete_table('core_map')

        # Deleting model 'User'
        db.delete_table('core_user')

        # Deleting model 'Place'
        db.delete_table('core_place')


    models = {
        'core.geography': {
            'Meta': {'object_name': 'Geography'},
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.map': {
            'Meta': {'object_name': 'Map'},
            'a_geography': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Geography']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.place': {
            'Meta': {'object_name': 'Place'},
            'a_geography': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Geography']", 'blank': 'True'}),
            'a_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Location']", 'blank': 'True'}),
            'a_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Tag']", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']