# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('A', 'Very Important'), ('B', 'Fairly Important'), ('C', 'Important')], max_length=50)),
                ('purchased', models.PositiveIntegerField(verbose_name='Quantity Purchased')),
                ('ok', models.PositiveIntegerField(null=True, editable=False, verbose_name='OK')),
                ('out', models.PositiveIntegerField(null=True, editable=False)),
                ('at_hand', models.PositiveIntegerField(null=True, editable=False)),
                ('still_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'inventory',
            },
        ),
    ]
