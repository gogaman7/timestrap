# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0005_auto_20170506_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='estimate',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
