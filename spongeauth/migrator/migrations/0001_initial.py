# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 16:03
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255, null=True)),
                ('mc_username', models.CharField(max_length=255)),
                ('irc_nick', models.CharField(max_length=255)),
                ('gh_username', models.CharField(max_length=255)),
                ('is_email_confirmed', models.BooleanField()),
                ('totp_secret', models.CharField(max_length=255)),
                ('is_totp_confirmed', models.BooleanField()),
                ('salt', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField()),
                ('failed_totp_attempts', models.IntegerField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('avatar_url', models.CharField(max_length=255)),
                ('join_date', models.DateTimeField()),
                ('google_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
                'managed': settings.IS_TESTING,
            },
        ),
    ]