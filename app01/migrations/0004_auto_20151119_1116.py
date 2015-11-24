# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app01.models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_app01_uploadstructuremodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='app01_uploadstructuremodel',
            name='commands',
            field=models.TextField(max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='app01_uploadstructuremodel',
            name='structurefile',
            field=models.FileField(upload_to=app01.models.upload_path_handler),
        ),
    ]
