# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.TextField(default=1)),
                ('title', models.CharField(max_length=200, verbose_name='default Title')),
                ('body', models.TextField(default='Body of post goes here')),
            ],
        ),
        migrations.DeleteModel(
            name='Family',
        ),
    ]
