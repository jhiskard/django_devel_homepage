# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0008_auto_20151124_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='end_as',
            field=models.CharField(default=b'M.S.', max_length=50, null=True, blank=True, choices=[(b'Postdoc.', b'Postdoc.'), (b'Ph.D.', b'Ph.D.'), (b'M.S.', b'M.S.'), (b'B.S.', b'B.S.'), (b'Co-advised', b'Co-advised')]),
        ),
    ]
