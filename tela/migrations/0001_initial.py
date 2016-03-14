# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.CharField(verbose_name='Latitude', max_length=20, blank=True, null=True)),
                ('location_longitude', models.CharField(verbose_name='latitude', max_length=20, blank=True, null=True)),
            ],
        ),
    ]
