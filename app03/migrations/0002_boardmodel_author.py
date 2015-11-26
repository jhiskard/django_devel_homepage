# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='author',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
