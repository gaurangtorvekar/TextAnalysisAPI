# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_profiles', '0003_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256, null=True)),
                ('country', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
