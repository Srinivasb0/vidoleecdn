# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_videomanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoManager',
        ),
        migrations.RemoveField(
            model_name='video',
            name='active',
        ),
        migrations.RemoveField(
            model_name='video',
            name='feautured',
        ),
        migrations.RemoveField(
            model_name='video',
            name='free_preview',
        ),
    ]
