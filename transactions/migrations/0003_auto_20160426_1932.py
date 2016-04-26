# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0001_initial'),
        ('transactions', '0002_auto_20160426_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='object_id',
        ),
        migrations.AddField(
            model_name='checkout',
            name='facilitator',
            field=models.ForeignKey(default=1, to='tela.Facilitator'),
            preserve_default=False,
        ),
    ]
