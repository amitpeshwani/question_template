# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0015_auto_20180601_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('mcq', 'Single Correct Choice'), ('mcc', 'Multiple Correct Choices'), ('code', 'Code'), ('upload', 'Assignment Upload'), ('integer', 'Answer in Integer'), ('string', 'Answer in String'), ('float', 'Answer in Float'), ('arrange', 'Arrange in Correct Order')], max_length=24),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='type',
            field=models.CharField(choices=[('standardtestcase', 'Standard Testcase'), ('stdiobasedtestcase', 'StdIO Based Testcase'), ('mcqtestcase', 'MCQ Testcase'), ('hooktestcase', 'Hook Testcase'), ('integertestcase', 'Integer Testcase'), ('stringtestcase', 'String Testcase'), ('floattestcase', 'Float Testcase'), ('arrangetestcase', 'Arrange Testcase'), ('easystandardtestcase', 'Easy Standard Testcase')], max_length=24, null=True),
        ),
    ]
