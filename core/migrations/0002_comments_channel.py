# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='channel',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]