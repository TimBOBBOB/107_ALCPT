# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_remove_exam_dtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='dtime',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 12, 4, 57, 254790, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
