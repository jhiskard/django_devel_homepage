# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app04', '0003_auto_20151126_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structuremodel',
            name='user',
        ),
    ]
