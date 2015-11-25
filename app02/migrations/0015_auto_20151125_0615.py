# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0014_auto_20151125_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='endtime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
