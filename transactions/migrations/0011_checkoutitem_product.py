# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160427_2111'),
        ('transactions', '0010_remove_checkoutitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutitem',
            name='product',
            field=models.ForeignKey(related_name='checked_out_items', default=1, to='inventory.Product'),
            preserve_default=False,
        ),
    ]
