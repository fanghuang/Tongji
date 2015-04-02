# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150328_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=2, null=True, choices=[(b'PROF', b'Professor'), (b'ASSO', b'Associate Professor'), (b'ASSI', b'Assistant Professor'), (b'INST', b'Instructor')]),
            preserve_default=True,
        ),
    ]
