# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-01 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0014_auto_20180601_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(blank=True, choices=[('mcq', 'Single Correct Choice'), ('mcc', 'Multiple Correct Choices'), ('code', 'Code'), ('upload', 'Assignment Upload'), ('integer', 'Answer in Integer'), ('string', 'Answer in String'), ('float', 'Answer in Float'), ('arrange', 'Arrange in Correct Order')], max_length=24),
        ),
    ]