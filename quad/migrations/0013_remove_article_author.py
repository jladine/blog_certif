# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quad', '0012_auto_20160823_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
