# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='grade',
            new_name='credit',
        ),
    ]
