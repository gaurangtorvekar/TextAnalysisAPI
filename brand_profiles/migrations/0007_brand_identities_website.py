# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_profiles', '0006_auto_20141128_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand_identities',
            name='website',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
