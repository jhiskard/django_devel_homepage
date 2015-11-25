# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import app02.models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0010_auto_20151124_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('contents', models.TextField(max_length=5000, blank=True)),
                ('attached', models.ImageField(upload_to=app02.models.upload_path_handler_news, blank=True)),
                ('is_activ', models.BooleanField(default=True)),
            ],
        ),
    ]
