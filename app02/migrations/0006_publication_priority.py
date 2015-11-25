# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0005_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
