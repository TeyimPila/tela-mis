# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('item', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('category', models.CharField(max_length=50, choices=[('A', 'Very Important'), ('B', 'Fairly Important'), ('C', 'Important')])),
                ('purchased', models.PositiveIntegerField(verbose_name='Quantity Purchased')),
                ('damaged', models.PositiveIntegerField(null=True, editable=False)),
                ('ok', models.PositiveIntegerField(null=True, editable=False, verbose_name='OK')),
                ('out', models.PositiveIntegerField(null=True, editable=False)),
                ('at_hand', models.PositiveIntegerField(null=True, editable=False)),
                ('still_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
