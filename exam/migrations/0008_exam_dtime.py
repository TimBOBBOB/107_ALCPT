# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20180418_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='dtime',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 11, 53, 21, 344495, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
