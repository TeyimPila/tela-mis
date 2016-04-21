# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0002_auto_20160408_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 12, 2, 35, 456983, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 12, 2, 49, 617813, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='location_latitude',
            field=models.FloatField(verbose_name='Latitude', blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='location_longitude',
            field=models.FloatField(verbose_name='Longitude', blank=True, max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='check_in_status',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='facilitator',
        ),
    ]
