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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('beneficiary_id', models.CharField(max_length=20)),
                ('beneficiary_name', models.CharField(max_length=225)),
                ('is_in_school', models.BinaryField(default=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
            ],
            options={
                'verbose_name_plural': 'Beneficiaries',
            },
        ),
    ]
