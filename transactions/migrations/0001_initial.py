# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('check_in_complete', models.BooleanField(default=False)),
                ('facilitator', models.ForeignKey(to='tela.Facilitator')),
            ],
            options={
                'ordering': ('-checkout_date',),
            },
        ),
        migrations.CreateModel(
            name='CheckoutItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('satatus', models.CharField(max_length=20, default='OK', choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')])),
                ('checkout', models.ForeignKey(to='transactions.Checkout', related_name='items')),
                ('product', models.ForeignKey(to='inventory.Product', related_name='checked_out_items')),
            ],
        ),
    ]
