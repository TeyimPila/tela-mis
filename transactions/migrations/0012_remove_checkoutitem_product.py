# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_checkoutitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutitem',
            name='product',
        ),
    ]
