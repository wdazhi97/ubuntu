# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-05 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0004_auto_20170903_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='web',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
