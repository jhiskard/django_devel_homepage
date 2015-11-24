# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='doi',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='issue',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
