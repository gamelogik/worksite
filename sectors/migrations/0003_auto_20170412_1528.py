# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-12 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0002_job'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['order']},
        ),
    ]