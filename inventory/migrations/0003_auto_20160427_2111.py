# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20160427_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchased',
            field=models.PositiveIntegerField(verbose_name='Purchased'),
        ),
    ]
