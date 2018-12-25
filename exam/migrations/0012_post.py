# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_remove_exam_dtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField(max_length=200)),
                ('text', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
