# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_profiles', '0002_auto_20141018_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField()),
                ('sentiment_score', models.NullBooleanField()),
                ('subjectivity', models.NullBooleanField()),
                ('objectivity', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
