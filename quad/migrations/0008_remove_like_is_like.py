# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quad', '0007_auto_20160816_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='is_like',
        ),
    ]
