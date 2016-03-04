# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_profiles', '0004_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='brand',
            field=models.ForeignKey(to='brand_profiles.Brands', null=True),
            preserve_default=True,
        ),
    ]
