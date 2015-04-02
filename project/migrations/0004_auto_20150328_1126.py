# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150328_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='approved_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='finished_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
