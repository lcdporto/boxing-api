# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-04 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_lending'),
    ]

    operations = [
        migrations.AddField(
            model_name='lending',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
            preserve_default=False,
        ),
    ]