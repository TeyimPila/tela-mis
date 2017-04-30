# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='still_available',
            new_name='available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='item',
            new_name='name',
        ),
    ]
