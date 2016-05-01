# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20160427_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='name',
            field=models.CharField(null=True, max_length=300, editable=False),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', verbose_name='Collected by'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='Individual'),
        ),
    ]
