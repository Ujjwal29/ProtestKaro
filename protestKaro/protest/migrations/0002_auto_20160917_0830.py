# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='aadhar_no',
            field=models.IntegerField(),
        ),
    ]
