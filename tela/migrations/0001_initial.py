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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('group_size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('serial_num', models.CharField(unique=True, max_length=20)),
                ('equipment_type', models.CharField(choices=[('Radio', 'Radio'), ('Tablet', 'Tablet'), ('Mat', 'Mat'), ('Workbook', 'Workbook')], max_length=15)),
                ('status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], default='OK', max_length=7)),
                ('check_in_status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], blank=True, default='OK', max_length=7, null=True)),
                ('check_out_date', models.DateTimeField(blank=True, null=True)),
                ('check_in_date', models.DateTimeField(blank=True, null=True)),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Checked out', 'Checked Out')], max_length=12)),
            ],
            options={
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('lga', models.ForeignKey(to='tela.LocalGovArea', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostAssessment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tutorial_type', models.CharField(choices=[('Feed and Read', 'Feed and Read'), ('After School Tutorial', 'After School Tutorial'), ('Face to Face', 'Tutorial'), ('Radio Tutorial', 'Radio Tutorial')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.CharField(verbose_name='Latitude', blank=True, max_length=20, null=True)),
                ('location_longitude', models.CharField(verbose_name='longitude', blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='facilitator',
            field=models.ForeignKey(to='tela.Facilitator', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
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
            name='lga',
            field=models.ForeignKey(to='tela.LocalGovArea', verbose_name='Local Government Area', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together=set([('facilitator', 'serial_num')]),
        ),
    ]
