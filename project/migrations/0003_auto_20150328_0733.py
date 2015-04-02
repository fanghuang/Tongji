# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150323_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(db_constraint=False, to='account.Student', related_name='involved_project'),
            preserve_default=True,
        ),
    ]
