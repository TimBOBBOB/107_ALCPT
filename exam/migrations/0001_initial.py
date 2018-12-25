# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('topic', models.TextField()),
                ('ddate', models.DateField()),
                ('member', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam_administrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examinees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Class', models.IntegerField(blank=True, default=1)),
                ('Sex', models.CharField(max_length=3, blank=True)),
                ('Major', models.CharField(max_length=6, blank=True)),
                ('Company', models.IntegerField(blank=True, default=1)),
                ('Comp_Num', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='grammar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.TextField(max_length=200)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=4)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='noun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.TextField(max_length=200)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=4)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions_bank_administrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions_bank_operator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.TextField(max_length=200)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=4)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score_reviewers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='short_conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.FileField(upload_to='documents/')),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=4)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='System_administrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.FileField(upload_to='documents/')),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=4)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Username', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=20)),
                ('FullName', models.CharField(max_length=5, blank=True)),
                ('Authority', models.CharField(max_length=25)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='system_administrator',
            name='user',
            field=models.OneToOneField(related_name='SA', to='exam.UserProfile'),
        ),
        migrations.AddField(
            model_name='score_reviewers',
            name='user',
            field=models.OneToOneField(related_name='SR', to='exam.UserProfile'),
        ),
        migrations.AddField(
            model_name='questions_bank_operator',
            name='user',
            field=models.OneToOneField(related_name='QBO', to='exam.UserProfile'),
        ),
        migrations.AddField(
            model_name='questions_bank_administrator',
            name='user',
            field=models.OneToOneField(related_name='QBA', to='exam.UserProfile'),
        ),
        migrations.AddField(
            model_name='examinees',
            name='user',
            field=models.OneToOneField(related_name='EE', to='exam.UserProfile'),
        ),
        migrations.AddField(
            model_name='exam_administrator',
            name='user',
            field=models.OneToOneField(related_name='EA', to='exam.UserProfile'),
        ),
    ]
