# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_damaged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
