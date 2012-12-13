# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('core_tag')

        # Deleting model 'Place'
        db.delete_table('core_place')

        # Deleting model 'Geography'
        db.delete_table('core_geography')

        # Deleting model 'Map'
        db.delete_table('core_map')

        # Deleting model 'User'
        db.delete_table('core_user')

        # Adding model 'Country'
        db.create_table('core_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Country'])

        # Adding model 'City'
        db.create_table('core_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Country'])),
        ))
        db.send_create_signal('core', ['City'])

        # Adding model 'Location'
        db.create_table('core_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instagram_id', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.City'])),
        ))
        db.send_create_signal('core', ['Location'])



    def backwards(self, orm):
        # Adding model 'Tag'
        db.create_table('core_tag', (
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Tag'])

        # Adding model 'Place'
        db.create_table('core_place', (
            ('province', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_geography', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Geography'], blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Tag'], blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Location'], blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Place'])

        # Adding model 'Geography'
        db.create_table('core_geography', (
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('distance', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Geography'])

        # Adding model 'Map'
        db.create_table('core_map', (
            ('map_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('a_geography', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Geography'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Map'])

        # Adding model 'User'
        db.create_table('core_user', (
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['User'])

        # Deleting model 'Country'
        db.delete_table('core_country')

        # Deleting model 'City'
        db.delete_table('core_city')

        # Deleting model 'Location'
        db.delete_table('core_location')



    models = {
        'core.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']