# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20180330_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Exam_Date', models.DateTimeField()),
                ('Error_Num', models.TextField(max_length=100, blank=True)),
                ('Score', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='examinees',
            name='Company',
            field=models.ForeignKey(to='exam.Company'),
        ),
        migrations.AlterField(
            model_name='examinees',
            name='Major',
            field=models.ForeignKey(to='exam.Department'),
        ),
        migrations.AddField(
            model_name='score',
            name='Ex',
            field=models.ForeignKey(null=True, to='exam.Examinees', to_field='user'),
        ),
    ]
