# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0003_auto_20160427_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('check_in_complete', models.BooleanField(editable=False, default=False)),
                ('object_id', models.PositiveIntegerField(verbose_name='Individual')),
                ('name', models.CharField(null=True, max_length=300, editable=False)),
                ('content_type', models.ForeignKey(verbose_name='Collected by', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-checkout_date',),
            },
        ),
        migrations.CreateModel(
            name='CheckoutItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], max_length=20, default='OK')),
                ('checkout', models.ForeignKey(related_name='items', to='transactions.Checkout')),
                ('product', models.ForeignKey(related_name='checked_out_items', to='inventory.Product')),
            ],
        ),
    ]
