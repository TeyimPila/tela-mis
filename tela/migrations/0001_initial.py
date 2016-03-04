# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('serial_number', models.CharField(unique=True, max_length=20)),
                ('equipment_type', models.CharField(choices=[('R', 'Radio'), ('T', 'Tablet'), ('M', 'Mat'), ('W', 'Workbook')], max_length=15)),
                ('status', models.CharField(choices=[('O', 'OK'), ('M', 'Missing'), ('D', 'Damaged')], max_length=1)),
                ('check_out_date', models.DateTimeField(null=True, blank=True)),
                ('check_in_date', models.DateTimeField(null=True, blank=True)),
                ('given_out', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'equipment',
            },
        ),
    ]
