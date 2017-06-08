# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-12 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sectors.Sector')),
            ],
        ),
    ]
