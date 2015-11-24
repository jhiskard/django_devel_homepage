# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20151119_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app01_uploadstructuremodel',
            name='commands',
            field=models.TextField(default=b'# Your initial structure was already loaded in "atoms", i.e, \n# atoms = io.read_xyz(\'your file\')\n# After manipulation, the final name of your AtomsSystem object should be "atoms".\n', max_length=10000, blank=True),
        ),
    ]
