# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app02.models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0004_auto_20151123_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.ImageField(upload_to=app02.models.upload_path_handler, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'Students', max_length=50, choices=[(b'Research Staff', b'Research Staff'), (b'Students', b'Students'), (b'Staff', b'Staff')])),
                ('degree', models.CharField(default=b'M.S. Candidate', max_length=50, choices=[(b'Research Professor', b'Research Professor'), (b'Ph.D. Candidate', b'Ph.D. Candidate'), (b'M.S. Candidate', b'M.S. Candidate'), (b'Graduate Research Assistant', b'Graduate Research Assistant'), (b'Secretary', b'Secretary')])),
                ('fields', models.TextField(max_length=200, null=True, blank=True)),
                ('office', models.TextField(max_length=200, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('tel', models.CharField(max_length=50, null=True, blank=True)),
                ('is_graduate', models.BooleanField(default=False)),
                ('end_as', models.CharField(default=b'M.S.', max_length=50, choices=[(b'Postdoc.', b'Postdoc.'), (b'Ph.D.', b'Ph.D.'), (b'M.S.', b'M.S.'), (b'B.S.', b'B.S.'), (b'Co-advised', b'Co-advised')])),
                ('currentposition', models.TextField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
