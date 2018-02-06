# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180131_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='classification',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_link',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]