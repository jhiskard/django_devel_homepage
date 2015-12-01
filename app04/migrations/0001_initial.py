# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import app04.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='app01_UploadStructureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('structurefile', models.FileField(upload_to=app04.models.upload_path_handler)),
                ('description', models.TextField(max_length=5000, blank=True)),
                ('commands', models.TextField(default=b'# Your initial structure was already loaded in "atoms", i.e, \n# atoms = io.read_xyz(\'your file\')\n# After manipulation, the final name of your AtomsSystem object should be "atoms".\n', max_length=10000, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
