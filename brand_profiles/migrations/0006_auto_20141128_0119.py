# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_profiles', '0005_reviews_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_Identities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256, null=True)),
                ('country', models.CharField(max_length=256, null=True)),
                ('email', models.CharField(max_length=256, null=True)),
                ('contact_number', models.CharField(max_length=256, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promotion', models.CharField(max_length=256, null=True)),
                ('duration', models.DateTimeField()),
                ('brand', models.ForeignKey(to='brand_profiles.Brand_Identities', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True)),
                ('classification_tag', models.CharField(max_length=256, null=True)),
                ('opening_time', models.DateTimeField()),
                ('cloasing_time', models.DateTimeField()),
                ('average_duration', models.CharField(max_length=256, null=True)),
                ('pricing', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('availabile_spots', models.IntegerField(default=0)),
                ('booking_capacity', models.IntegerField(default=0)),
                ('filled_capacity', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(to='brand_profiles.Brand_Identities', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='promotions',
            name='tour',
            field=models.ForeignKey(to='brand_profiles.Tours', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reviews',
            name='classification_tag',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='brand',
            field=models.ForeignKey(to='brand_profiles.Brand_Identities', null=True),
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
    ]
