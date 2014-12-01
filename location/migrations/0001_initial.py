# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='City/Location name')),
                ('abbr', models.CharField(max_length=10, null=True, verbose_name='City/Location Abbreviation', blank=True)),
                ('latitude', models.CharField(max_length=60, null=True, verbose_name='City/Location latitude', blank=True)),
                ('longitude', models.CharField(max_length=60, null=True, verbose_name='City/Location longitude', blank=True)),
                ('timezone', models.CharField(max_length=60, null=True, verbose_name='City/Location timezone', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'City/Location',
                'verbose_name_plural': 'Cities/Locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso2_code', models.CharField(max_length=2, null=True, verbose_name='ISO alpha-2', blank=True)),
                ('name', models.CharField(max_length=128, verbose_name='Official name (CAPS)')),
                ('printable_name', models.CharField(max_length=128, verbose_name='Country name')),
                ('iso3_code', models.CharField(max_length=3, null=True, verbose_name='ISO alpha-3', blank=True)),
                ('numcode', models.CharField(max_length=100, null=True, verbose_name='ISO numeric', blank=True)),
                ('fips_104', models.CharField(max_length=100, null=True, verbose_name='FIPS 10-4', blank=True)),
                ('internet', models.CharField(max_length=100, null=True, verbose_name='Intenet', blank=True)),
                ('capital', models.CharField(max_length=100, null=True, verbose_name='Capital', blank=True)),
                ('map_reference', models.CharField(max_length=100, null=True, verbose_name='Map Reference', blank=True)),
                ('nationality_singular', models.CharField(max_length=100, null=True, verbose_name='Nationality Singular', blank=True)),
                ('nationality_plural', models.CharField(max_length=100, null=True, verbose_name='Nationality Plural', blank=True)),
                ('currency', models.CharField(max_length=100, null=True, verbose_name='Currency', blank=True)),
                ('currency_code', models.CharField(max_length=100, null=True, verbose_name='Currency code', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='State/Province name')),
                ('abbr', models.CharField(max_length=10, null=True, verbose_name='State/Province Abbreviation', blank=True)),
                ('adm1_code', models.CharField(max_length=60, null=True, verbose_name='State/Province ADM1 code', blank=True)),
                ('country', models.ForeignKey(to='location.Country')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'State/Province',
                'verbose_name_plural': 'States/Provinces',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='location.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='location.State'),
            preserve_default=True,
        ),
    ]
