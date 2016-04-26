# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutitem',
            old_name='satatus',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='facilitator',
        ),
        migrations.AddField(
            model_name='checkout',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
