# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0003_publication_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='published_date',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='published_month',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
