# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('aadhar_no', models.IntegerField(max_length=12)),
            ],
        ),
    ]
