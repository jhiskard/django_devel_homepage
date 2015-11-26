# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0002_boardmodel_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BoardModel',
        ),
    ]
