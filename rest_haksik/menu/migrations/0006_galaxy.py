# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-11 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galaxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('menu', models.TextField()),
            ],
        ),
    ]