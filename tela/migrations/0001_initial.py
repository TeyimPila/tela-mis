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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('group_size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(unique=True, max_length=20)),
                ('equipment_type', models.CharField(choices=[('Radio', 'Radio'), ('Tablet', 'Tablet'), ('Mat', 'Mat'), ('Workbook', 'Workbook')], max_length=15)),
                ('status', models.CharField(default='OK', choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], max_length=7)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('lga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Local Government Area', to='tela.LocalGovArea')),
            ],
        ),
        migrations.CreateModel(
            name='PostAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Beneficiary')),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Beneficiary')),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('tutor_id', models.CharField(max_length=9)),
                ('major', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_type', models.CharField(choices=[('Feed and Read', 'Feed and Read'), ('After School Tutorial', 'After School Tutorial'), ('Face to Face', 'Tutorial'), ('Radio Tutorial', 'Radio Tutorial')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.FloatField(null=True, verbose_name='Latitude', max_length=20, blank=True)),
                ('location_longitude', models.FloatField(null=True, verbose_name='Longitude', max_length=20, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='facilitator',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Neighborhood', blank=True),
        ),
        migrations.AddField(
            model_name='enumerator',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Neighborhood'),
        ),
        migrations.AddField(
            model_name='center',
            name='facilitator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Facilitator'),
        ),
        migrations.AddField(
            model_name='center',
            name='tutorial_types',
            field=models.ManyToManyField(to='tela.TutorialType'),
        ),
        migrations.AddField(
            model_name='center',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Venue'),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Center'),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.Neighborhood'),
        ),
    ]
