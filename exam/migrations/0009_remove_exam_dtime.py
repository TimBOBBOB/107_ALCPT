# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_exam_dtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='dtime',
        ),
    ]
