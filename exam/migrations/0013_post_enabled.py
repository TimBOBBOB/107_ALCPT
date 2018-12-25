# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
