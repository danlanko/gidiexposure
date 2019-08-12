# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-23 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0007_auto_20190323_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageview',
            name='position',
            field=models.CharField(choices=[('Left Bottom', 'Left Bottom'), ('Left Top', 'Left Top'), ('Right Bottom', 'Right Bottom'), ('Center', 'Center'), ('Right Top', 'Right Top')], max_length=20, unique=True),
        ),
    ]
