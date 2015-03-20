# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('grade', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=1, choices=[(b'A', b'A. School'), (b'B', b'B. University'), (b'C', b'C. Province'), (b'D', b'D. Nation')])),
                ('approved_time', models.DateTimeField()),
                ('finished_time', models.DateTimeField()),
                ('leader', models.ForeignKey(related_name='leading_project', to='account.Student')),
                ('members', models.ManyToManyField(related_name='involved_project', to='account.Student')),
                ('teacher', models.ForeignKey(to='account.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mark',
            name='project',
            field=models.ForeignKey(to='project.Project'),
            preserve_default=True,
        ),
    ]
