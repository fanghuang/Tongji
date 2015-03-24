# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(default=b'PROF', max_length=2, choices=[(b'PROF', b'Professor'), (b'ASSO', b'Associate Professor'), (b'ASSI', b'Assistant Professor'), (b'INST', b'Instructor')]),
            preserve_default=True,
        ),
    ]
