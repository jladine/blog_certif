# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quad', '0004_auto_20160730_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
