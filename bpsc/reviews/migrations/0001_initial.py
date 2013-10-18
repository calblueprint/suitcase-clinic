# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'reviews_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('reviewer', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'reviews', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'reviews_review')


    models = {
        u'reviews.review': {
            'Meta': {'object_name': 'Review'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'reviewer': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['reviews']