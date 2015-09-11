# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Varsinaissuomenpalvelut',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('kohde', models.CharField(max_length=50, null=True, blank=True)),
                ('postinumer', models.CharField(max_length=254, null=True, blank=True)),
                ('kunta', models.CharField(max_length=254, null=True, blank=True)),
                ('nimi', models.CharField(max_length=254, null=True, blank=True)),
                ('aukiolo', models.CharField(max_length=50, null=True, blank=True)),
                ('kunta_2011', models.CharField(max_length=254, null=True, blank=True)),
                ('lis_tiedot', models.CharField(max_length=254, null=True, db_column='lis\xe4tiedot', blank=True)),
                ('katuosoite', models.CharField(max_length=254, null=True, blank=True)),
                ('kuntanro', models.IntegerField(null=True, blank=True)),
                ('kohdenro', models.IntegerField(null=True, blank=True)),
                ('paikkaluku', models.IntegerField(null=True, blank=True)),
                ('julkpalvel', models.CharField(max_length=10, null=True, blank=True)),
                ('wwwlinkki', models.CharField(max_length=250, null=True, blank=True)),
                ('timestamp', models.DateField(null=True, blank=True)),
                ('paivittaja', models.CharField(max_length=50, null=True, blank=True)),
                ('puhelin', models.CharField(max_length=15, null=True, blank=True)),
                ('visual', models.CharField(max_length=250, null=True, blank=True)),
                ('legend', models.CharField(max_length=250, null=True, blank=True)),
                ('postinro', models.CharField(max_length=5, null=True, blank=True)),
                ('kohde2', models.CharField(max_length=80, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=3067, dim=4, null=True, blank=True)),
            ],
            options={
                'db_table': 'varsinaissuomenpalvelut',
                'managed': False,
            },
        ),
    ]
