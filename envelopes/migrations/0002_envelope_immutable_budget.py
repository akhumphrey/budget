# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envelopes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envelope',
            name='immutable_budget',
            field=models.BooleanField(default=True),
        ),
    ]
