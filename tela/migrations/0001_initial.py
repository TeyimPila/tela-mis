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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('beneficiary_id', models.CharField(max_length=20)),
                ('is_in_school', models.BooleanField(verbose_name='is in School?', default=True)),
            ],
            options={
                'verbose_name_plural': 'beneficiaries',
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('group_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('account_number', models.CharField(max_length=12, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('serial_num', models.CharField(unique=True, max_length=20)),
                ('equipment_type', models.CharField(choices=[('Radio', 'Radio'), ('Tablet', 'Tablet'), ('Mat', 'Mat'), ('Workbook', 'Workbook')], max_length=15)),
                ('status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], max_length=7, default='OK')),
                ('check_in_status', models.CharField(choices=[('OK', 'OK'), ('Missing', 'Missing'), ('Damaged', 'Damaged')], null=True, max_length=7, blank=True, default='OK')),
                ('check_out_date', models.DateTimeField(null=True, blank=True)),
                ('check_in_date', models.DateTimeField(null=True, blank=True)),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Checked out', 'Checked Out')], max_length=12)),
            ],
            options={
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('account_number', models.CharField(max_length=12, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalGovArea',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('neighborhood', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PostAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Beneficiary')),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Beneficiary')),
                ('enumerator', models.ForeignKey(to='tela.Enumerator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('tutor_id', models.CharField(max_length=9)),
                ('major', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TutorialType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tutorial_type', models.CharField(choices=[('Feed and Read', 'Feed and Read'), ('After School Tutorial', 'After School Tutorial'), ('Face to Face', 'Tutorial'), ('Radio Tutorial', 'Radio Tutorial')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('location_latitude', models.CharField(max_length=20, verbose_name='Latitude', null=True, blank=True)),
                ('location_longitude', models.CharField(max_length=20, verbose_name='longitude', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='facilitator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Facilitator', blank=True),
        ),
        migrations.AddField(
            model_name='center',
            name='facilitator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Facilitator'),
        ),
        migrations.AddField(
            model_name='center',
            name='tutorial_types',
            field=models.ManyToManyField(to='tela.TutorialType'),
        ),
        migrations.AddField(
            model_name='center',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Venue'),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='tela.Center'),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='lga',
            field=models.ForeignKey(verbose_name='Local Government Area', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tela.LocalGovArea'),
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together=set([('facilitator', 'serial_num')]),
        ),
    ]
