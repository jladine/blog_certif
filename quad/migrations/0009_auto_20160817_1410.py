# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quad', '0008_remove_like_is_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='quad.Comment'),
        ),
    ]