# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20160506_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='feautured',
            new_name='featured',
        ),
    ]
