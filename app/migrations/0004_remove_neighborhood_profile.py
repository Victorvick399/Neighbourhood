# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_business_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='profile',
        ),
    ]
