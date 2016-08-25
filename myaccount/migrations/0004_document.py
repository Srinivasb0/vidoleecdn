# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0003_auto_20160721_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myaccount.MyUser')),
            ],
        ),
    ]
