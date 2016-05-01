# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='center',
            field=models.ForeignKey(null=True, to='tela.Center'),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='neighborhood',
            field=models.ForeignKey(null=True, to='tela.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='center',
            name='facilitator',
            field=models.ForeignKey(null=True, to='tela.Facilitator'),
        ),
        migrations.AlterField(
            model_name='center',
            name='venue',
            field=models.ForeignKey(null=True, to='tela.Venue'),
        ),
        migrations.AlterField(
            model_name='enumerator',
            name='neighborhood',
            field=models.ForeignKey(null=True, to='tela.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='facilitator',
            name='neighborhood',
            field=models.ForeignKey(null=True, blank=True, to='tela.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='lga',
            field=models.ForeignKey(verbose_name='Local Government Area', null=True, to='tela.LocalGovArea'),
        ),
    ]
