# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-01 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]