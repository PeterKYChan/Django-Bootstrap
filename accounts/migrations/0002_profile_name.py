# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=datetime.datetime(2014, 12, 1, 11, 56, 1, 518491, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
