# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20150328_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'PENDING', max_length=10, choices=[(b'PENDING', 'A. PENDING'), (b'APPROVED', 'B. APPROVED'), (b'REJECTED', 'C. REJECTED')]),
            preserve_default=True,
        ),
    ]
