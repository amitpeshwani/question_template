# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0011_release_0_8_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='time_between_attempts',
            field=models.FloatField(default=0.0, verbose_name='Time Between Quiz Attempts in hours'),
        ),
    ]
