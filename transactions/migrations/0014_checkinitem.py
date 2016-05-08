# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160427_2111'),
        ('transactions', '0013_checkoutitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckinItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(max_length=20, choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], default='OK')),
                ('checkin', models.ForeignKey(related_name='+', to='transactions.Checkout')),
                ('product', models.ForeignKey(related_name='+', to='inventory.Product')),
            ],
        ),
    ]
