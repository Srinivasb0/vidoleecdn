# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_auto_20160523_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='share_message',
            field=models.TextField(default='DEFAULT_MESSAGE'),
        ),
    ]
