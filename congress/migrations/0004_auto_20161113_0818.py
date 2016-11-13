# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-13 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0003_auto_20161113_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='party',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter_username',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
