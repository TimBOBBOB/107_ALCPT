# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20180403_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Name',
            field=models.CharField(max_length=200),
        ),
    ]
