# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
    ]
