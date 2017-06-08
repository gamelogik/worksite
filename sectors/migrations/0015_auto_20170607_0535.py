# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0014_question_prompt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cvs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('motivation', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='sector',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
