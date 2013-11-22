# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HousingTag'
        db.create_table(u'search_housingtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'search', ['HousingTag'])

        # Adding unique constraint on 'HousingTag', fields ['tag_type', 'value']
        db.create_unique(u'search_housingtag', ['tag_type', 'value'])

        # Adding model 'CommunityTag'
        db.create_table(u'search_communitytag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'search', ['CommunityTag'])

        # Adding unique constraint on 'CommunityTag', fields ['tag_type', 'value']
        db.create_unique(u'search_communitytag', ['tag_type', 'value'])

        # Adding model 'EmploymentTag'
        db.create_table(u'search_employmenttag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'search', ['EmploymentTag'])

        # Adding unique constraint on 'EmploymentTag', fields ['tag_type', 'value']
        db.create_unique(u'search_employmenttag', ['tag_type', 'value'])

        # Adding model 'LegalTag'
        db.create_table(u'search_legaltag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'search', ['LegalTag'])

        # Adding unique constraint on 'LegalTag', fields ['tag_type', 'value']
        db.create_unique(u'search_legaltag', ['tag_type', 'value'])

        # Adding model 'HousingResource'
        db.create_table(u'search_housingresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('num_used', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('auto_added', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted', self.gf('django.db.models.fields.DateField')()),
            ('outdated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'search', ['HousingResource'])

        # Adding M2M table for field tags on 'HousingResource'
        m2m_table_name = db.shorten_name(u'search_housingresource_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('housingresource', models.ForeignKey(orm[u'search.housingresource'], null=False)),
            ('housingtag', models.ForeignKey(orm[u'search.housingtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['housingresource_id', 'housingtag_id'])

        # Adding model 'CommunityResource'
        db.create_table(u'search_communityresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('num_used', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('auto_added', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted', self.gf('django.db.models.fields.DateField')()),
            ('outdated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'search', ['CommunityResource'])

        # Adding M2M table for field tags on 'CommunityResource'
        m2m_table_name = db.shorten_name(u'search_communityresource_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('communityresource', models.ForeignKey(orm[u'search.communityresource'], null=False)),
            ('communitytag', models.ForeignKey(orm[u'search.communitytag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['communityresource_id', 'communitytag_id'])

        # Adding model 'EmploymentResource'
        db.create_table(u'search_employmentresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('num_used', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('auto_added', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted', self.gf('django.db.models.fields.DateField')()),
            ('outdated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('listing_of_the_week', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'search', ['EmploymentResource'])

        # Adding M2M table for field tags on 'EmploymentResource'
        m2m_table_name = db.shorten_name(u'search_employmentresource_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employmentresource', models.ForeignKey(orm[u'search.employmentresource'], null=False)),
            ('employmenttag', models.ForeignKey(orm[u'search.employmenttag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employmentresource_id', 'employmenttag_id'])

        # Adding model 'LegalResource'
        db.create_table(u'search_legalresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('num_used', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('auto_added', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'search', ['LegalResource'])

        # Adding M2M table for field tags on 'LegalResource'
        m2m_table_name = db.shorten_name(u'search_legalresource_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('legalresource', models.ForeignKey(orm[u'search.legalresource'], null=False)),
            ('legaltag', models.ForeignKey(orm[u'search.legaltag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['legalresource_id', 'legaltag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'LegalTag', fields ['tag_type', 'value']
        db.delete_unique(u'search_legaltag', ['tag_type', 'value'])

        # Removing unique constraint on 'EmploymentTag', fields ['tag_type', 'value']
        db.delete_unique(u'search_employmenttag', ['tag_type', 'value'])

        # Removing unique constraint on 'CommunityTag', fields ['tag_type', 'value']
        db.delete_unique(u'search_communitytag', ['tag_type', 'value'])

        # Removing unique constraint on 'HousingTag', fields ['tag_type', 'value']
        db.delete_unique(u'search_housingtag', ['tag_type', 'value'])

        # Deleting model 'HousingTag'
        db.delete_table(u'search_housingtag')

        # Deleting model 'CommunityTag'
        db.delete_table(u'search_communitytag')

        # Deleting model 'EmploymentTag'
        db.delete_table(u'search_employmenttag')

        # Deleting model 'LegalTag'
        db.delete_table(u'search_legaltag')

        # Deleting model 'HousingResource'
        db.delete_table(u'search_housingresource')

        # Removing M2M table for field tags on 'HousingResource'
        db.delete_table(db.shorten_name(u'search_housingresource_tags'))

        # Deleting model 'CommunityResource'
        db.delete_table(u'search_communityresource')

        # Removing M2M table for field tags on 'CommunityResource'
        db.delete_table(db.shorten_name(u'search_communityresource_tags'))

        # Deleting model 'EmploymentResource'
        db.delete_table(u'search_employmentresource')

        # Removing M2M table for field tags on 'EmploymentResource'
        db.delete_table(db.shorten_name(u'search_employmentresource_tags'))

        # Deleting model 'LegalResource'
        db.delete_table(u'search_legalresource')

        # Removing M2M table for field tags on 'LegalResource'
        db.delete_table(db.shorten_name(u'search_legalresource_tags'))


    models = {
        u'search.communityresource': {
            'Meta': {'ordering': "['auto_added']", 'object_name': 'CommunityResource'},
            'auto_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_used': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'outdated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.CommunityTag']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'search.communitytag': {
            'Meta': {'ordering': "['tag_type', 'value']", 'unique_together': "(('tag_type', 'value'),)", 'object_name': 'CommunityTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'search.employmentresource': {
            'Meta': {'ordering': "['auto_added', '-posted']", 'object_name': 'EmploymentResource'},
            'auto_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'listing_of_the_week': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_used': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'outdated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.EmploymentTag']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'search.employmenttag': {
            'Meta': {'ordering': "['tag_type', 'value']", 'unique_together': "(('tag_type', 'value'),)", 'object_name': 'EmploymentTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'search.housingresource': {
            'Meta': {'ordering': "['auto_added', '-posted']", 'object_name': 'HousingResource'},
            'auto_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_used': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'outdated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.HousingTag']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'search.housingtag': {
            'Meta': {'ordering': "['tag_type', 'value']", 'unique_together': "(('tag_type', 'value'),)", 'object_name': 'HousingTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'search.legalresource': {
            'Meta': {'ordering': "['auto_added']", 'object_name': 'LegalResource'},
            'auto_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_used': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.LegalTag']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'search.legaltag': {
            'Meta': {'ordering': "['tag_type', 'value']", 'unique_together': "(('tag_type', 'value'),)", 'object_name': 'LegalTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['search']