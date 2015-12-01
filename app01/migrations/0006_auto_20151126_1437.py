# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20151120_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app01_uploadstructuremodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='app01_UploadStructureModel',
        ),
    ]
