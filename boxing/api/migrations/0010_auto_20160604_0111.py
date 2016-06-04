# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-04 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20160603_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='avatar',
            field=models.CharField(default='default/item_avatar.png', max_length=100),
        ),
    ]
