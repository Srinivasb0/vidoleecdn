# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0008_auto_20160721_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
