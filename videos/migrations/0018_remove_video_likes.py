# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0017_video_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
    ]
