# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0011_auto_20160726_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='document',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='document',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='document',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='document',
            name='url',
        ),
    ]
