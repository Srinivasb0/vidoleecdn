# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-07 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0022_video_product_embed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='product_embed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
