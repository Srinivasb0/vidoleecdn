# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20160728_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
