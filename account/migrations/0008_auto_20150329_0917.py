# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20150328_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11, null=True, verbose_name='Phone', blank=True),
            preserve_default=True,
        ),
    ]
