# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20151123_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='abstract',
            field=models.TextField(max_length=50000, blank=True),
        ),
    ]
