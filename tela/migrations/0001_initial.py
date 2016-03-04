# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('beneficiary_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('is_in_school', models.BooleanField(verbose_name='is in School?', default=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('year_of_birth', models.IntegerField(verbose_name='year of birth', default=2016)),
            ],
            options={
                'verbose_name_plural': 'beneficiaries',
            },
        ),
    ]
