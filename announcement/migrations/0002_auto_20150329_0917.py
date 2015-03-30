# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='url',
            field=models.URLField(verbose_name='URL'),
            preserve_default=True,
        ),
    ]
