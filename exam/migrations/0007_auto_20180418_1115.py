# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20180418_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='test',
            new_name='text',
        ),
        migrations.AddField(
            model_name='member',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 3, 14, 53, 585874, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 3, 15, 12, 372642, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
