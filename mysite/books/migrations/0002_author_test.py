# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='test',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
