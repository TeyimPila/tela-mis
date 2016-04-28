# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('beneficiary_id', models.CharField(max_length=20)),
                ('is_in_school', models.BooleanField(verbose_name='is in School?', default=True)),
                ('age', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'beneficiaries',
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('group_size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('account_number', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('serial_num', models.CharField(max_length=20, unique=True)),
                ('equipment_type', models.CharField(choices=[('Radio', 'Radio'), ('Tablet', 'Tablet'), ('Mat', 'Mat'), ('Workbook', 'Workbook')], max_length=15)),
                ('status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], max_length=7, default='OK')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('account_number', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalGovArea',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('lga', models.ForeignKey(verbose_name='Local Government Area', on_delete=django.db.models.deletion.SET_NULL, to='tela.LocalGovArea', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostAssessment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Beneficiary', null=True)),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreAssessment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Beneficiary', null=True)),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('tutor_id', models.CharField(max_length=9)),
                ('major', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TutorialType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tutorial_type', models.CharField(choices=[('Feed and Read', 'Feed and Read'), ('After School Tutorial', 'After School Tutorial'), ('Face to Face', 'Tutorial'), ('Radio Tutorial', 'Radio Tutorial')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.FloatField(verbose_name='Latitude', blank=True, max_length=20, null=True)),
                ('location_longitude', models.FloatField(verbose_name='Longitude', blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='facilitator',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='tela.Neighborhood', null=True),
        ),
        migrations.AddField(
            model_name='enumerator',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Neighborhood', null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='facilitator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Facilitator', null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='tutorial_types',
            field=models.ManyToManyField(to='tela.TutorialType'),
        ),
        migrations.AddField(
            model_name='center',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Venue', null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Center', null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tela.Neighborhood', null=True),
        ),
    ]
