# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20150328_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'A', 'A. Department'), (b'B', 'B. University'), (b'C', 'C. Province'), (b'D', 'D. Nation')]),
            preserve_default=True,
        ),
    ]
