# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_link', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('html_content', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=1000, null=True)),
                ('tag', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
