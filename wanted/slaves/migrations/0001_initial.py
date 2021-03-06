# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_fname', models.CharField(max_length=15)),
                ('s_lname', models.CharField(max_length=15)),
                ('s_descr', models.TextField()),
                ('s_join_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=15)),
                ('r_descr', models.TextField()),
                ('join_date', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slaves.Master')),
            ],
        ),
        migrations.CreateModel(
            name='Slave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_fname', models.CharField(max_length=15)),
                ('s_lname', models.CharField(max_length=15)),
                ('s_descr', models.TextField()),
                ('s_join_date', models.DateField(auto_now=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
