# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='lga',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='neighborhood',
            field=models.ForeignKey(to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='enumerator',
            name='neighborhood',
            field=models.ForeignKey(to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='lga',
            field=models.ForeignKey(to='tela.LocalGovArea', on_delete=django.db.models.deletion.SET_NULL, null=True, verbose_name='Local Government Area'),
        ),
    ]
