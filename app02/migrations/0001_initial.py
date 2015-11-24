# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app02.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.ImageField(upload_to=app02.models.upload_path_handler, blank=True)),
                ('title', models.TextField(max_length=200)),
                ('authors', models.TextField(max_length=200)),
                ('journal', models.TextField(max_length=200)),
                ('year', models.IntegerField()),
                ('vol', models.IntegerField()),
                ('issue', models.IntegerField()),
                ('pages', models.TextField(max_length=200)),
                ('doi', models.TextField(max_length=200)),
                ('link', models.TextField(max_length=1000)),
            ],
        ),
    ]
