# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-13 06:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0006_auto_20170413_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='apply',
        ),
        migrations.DeleteModel(
            name='Apply',
        ),
    ]
