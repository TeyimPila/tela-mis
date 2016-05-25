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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])),
                ('beneficiary_id', models.CharField(max_length=20)),
                ('is_in_school', models.BooleanField(default=True, verbose_name='is in School?')),
                ('age', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'beneficiaries',
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('group_size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])),
                ('account_number', models.CharField(null=True, max_length=12, blank=True)),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('phone_number', models.CharField(null=True, max_length=15, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('serial_num', models.CharField(max_length=20, unique=True)),
                ('equipment_type', models.CharField(max_length=15, choices=[('Radio', 'Radio'), ('Tablet', 'Tablet'), ('Mat', 'Mat'), ('Workbook', 'Workbook')])),
                ('status', models.CharField(max_length=7, default='OK', choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')])),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])),
                ('account_number', models.CharField(null=True, max_length=12, blank=True)),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('phone_number', models.CharField(null=True, max_length=15, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalGovArea',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('lga', models.ForeignKey(to='tela.LocalGovArea', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Local Government Area', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(to='tela.Beneficiary', on_delete=django.db.models.deletion.SET_NULL, null=True)),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(to='tela.Beneficiary', on_delete=django.db.models.deletion.SET_NULL, null=True)),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])),
                ('tutor_id', models.CharField(max_length=9)),
                ('major', models.CharField(max_length=300)),
                ('classification', models.CharField(max_length=2, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')])),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
                ('phone_number', models.CharField(null=True, max_length=15, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TutorialType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tutorial_type', models.CharField(max_length=50, choices=[('Feed and Read', 'Feed and Read'), ('After School Tutorial', 'After School Tutorial'), ('Face to Face', 'Tutorial'), ('Radio Tutorial', 'Radio Tutorial')])),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.FloatField(null=True, max_length=20, blank=True, verbose_name='Latitude')),
                ('location_longitude', models.FloatField(null=True, max_length=20, blank=True, verbose_name='Longitude')),
            ],
        ),
        migrations.AddField(
            model_name='facilitator',
            name='neighborhood',
            field=models.ForeignKey(to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='enumerator',
            name='neighborhood',
            field=models.ForeignKey(to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='facilitator',
            field=models.ForeignKey(to='tela.Facilitator', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='tutorial_types',
            field=models.ManyToManyField(to='tela.TutorialType'),
        ),
        migrations.AddField(
            model_name='center',
            name='venue',
            field=models.ForeignKey(to='tela.Venue', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='center',
            field=models.ForeignKey(to='tela.Center', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='neighborhood',
            field=models.ForeignKey(to='tela.Neighborhood', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
