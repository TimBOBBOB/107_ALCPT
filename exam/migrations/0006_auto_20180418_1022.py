# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20180403_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('test', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='Name',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='department',
            name='Name',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='exam',
            name='ddate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='member',
            field=models.ForeignKey(to='exam.member'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='topic',
            field=models.ForeignKey(to='exam.topic'),
        ),
        migrations.AlterField(
            model_name='examinees',
            name='Company',
            field=models.ForeignKey(default=6, to='exam.Company'),
        ),
        migrations.AlterField(
            model_name='examinees',
            name='Major',
            field=models.ForeignKey(default=5, to='exam.Department'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='question',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='FullName',
            field=models.CharField(max_length=5, default='未修改'),
        ),
    ]
