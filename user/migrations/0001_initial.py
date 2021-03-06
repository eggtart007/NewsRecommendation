# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-02 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('news', '0005_auto_20180202_1313'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_raw', models.ImageField(default='', upload_to='upload/%Y%m%d', verbose_name='User upload avatar')),
                ('avatar_l', models.ImageField(default='', upload_to='avatar/%Y%m%d', verbose_name='large avatar')),
                ('avatar_m', models.ImageField(default='', upload_to='avatar/%Y%m%d', verbose_name='medium avatar')),
                ('avatar_s', models.ImageField(default='', upload_to='avatar/%Y%m%d', verbose_name='small avatar')),
            ],
        ),
        migrations.CreateModel(
            name='user_behavior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behavior_type', models.IntegerField(default=0)),
                ('is_comment', models.BooleanField(default=False)),
                ('is_collect', models.BooleanField(default=False)),
                ('behavior_way', models.IntegerField(default=1)),
                ('behavior_time', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
            options={
                'ordering': ['-behavior_time'],
            },
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('nickname', models.CharField(blank=True, max_length=256, null=True)),
                ('gender', models.IntegerField(default=-1)),
                ('birthday', models.DateField(null=True)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
                ('education', models.CharField(blank=True, max_length=256, null=True)),
                ('tag', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Avatar')),
            ],
        ),
        migrations.CreateModel(
            name='user_tag',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tag', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('news_society', models.FloatField(default=0)),
                ('news_tech', models.FloatField(default=0)),
                ('news_entertainment', models.FloatField(default=0)),
                ('news_game', models.FloatField(default=0)),
                ('news_sports', models.FloatField(default=0)),
                ('news_car', models.FloatField(default=0)),
                ('news_finance', models.FloatField(default=0)),
                ('news_funny', models.FloatField(default=0)),
                ('news_military', models.FloatField(default=0)),
                ('news_world', models.FloatField(default=0)),
                ('news_fashion', models.FloatField(default=0)),
                ('news_baby', models.FloatField(default=0)),
                ('news_history', models.FloatField(default=0)),
                ('news_food', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user_behavior',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='behavior', to=settings.AUTH_USER_MODEL),
        ),
    ]
