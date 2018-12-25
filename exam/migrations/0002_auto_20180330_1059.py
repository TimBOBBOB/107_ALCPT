# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammar',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noun',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reading',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='short_conversation',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talk',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='grammar',
            name='answer',
            field=models.CharField(max_length=4, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
        ),
        migrations.AlterField(
            model_name='noun',
            name='answer',
            field=models.CharField(max_length=4, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
        ),
        migrations.AlterField(
            model_name='reading',
            name='answer',
            field=models.CharField(max_length=4, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
        ),
        migrations.AlterField(
            model_name='short_conversation',
            name='answer',
            field=models.CharField(max_length=4, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
        ),
        migrations.AlterField(
            model_name='talk',
            name='answer',
            field=models.CharField(max_length=4, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
        ),
    ]
