# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170821_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]