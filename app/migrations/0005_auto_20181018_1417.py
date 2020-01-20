# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_neighborhood_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='Locality',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='locality',
            field=models.CharField(default='e.g Nairobi, Juja, Kiambu etc', max_length=30),
        ),
    ]