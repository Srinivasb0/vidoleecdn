# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0020_video_amazon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='amazon',
            new_name='product_img',
        ),
    ]
