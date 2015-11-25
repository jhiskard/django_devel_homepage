# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app02.models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0007_member_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='thumbnail',
            field=models.ImageField(upload_to=app02.models.upload_path_handler_member, blank=True),
        ),
    ]
