# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_auto_20160522_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
