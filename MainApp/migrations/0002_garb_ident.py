# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='garb',
            name='ident',
            field=models.IntegerField(default=0),
        ),
    ]