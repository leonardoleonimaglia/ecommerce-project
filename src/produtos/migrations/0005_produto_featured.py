# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-01 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20181201_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]