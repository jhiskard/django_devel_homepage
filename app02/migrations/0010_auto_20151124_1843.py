# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0009_auto_20151124_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='degree',
            field=models.CharField(default=b'M.S. Candidate', max_length=50, blank=True, choices=[(b'Research Professor', b'Research Professor'), (b'Ph.D. Candidate', b'Ph.D. Candidate'), (b'M.S. Candidate', b'M.S. Candidate'), (b'Graduate Research Assistant', b'Graduate Research Assistant'), (b'Secretary', b'Secretary')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(default=b'Students', max_length=50, blank=True, choices=[(b'Research Staff', b'Research Staff'), (b'Students', b'Students'), (b'Staff', b'Staff')]),
        ),
    ]
