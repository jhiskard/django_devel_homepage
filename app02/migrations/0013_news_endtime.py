# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0012_news_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='endtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
