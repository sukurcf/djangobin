# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0002_auto_20180616_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='lang_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Language Code'),
        ),
    ]
