# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150328_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default=b'', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=11, null=True),
            preserve_default=True,
        ),
    ]
