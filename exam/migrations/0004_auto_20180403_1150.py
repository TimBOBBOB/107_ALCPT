# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20180402_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Name',
            field=models.CharField(max_length=5),
        ),
    ]
