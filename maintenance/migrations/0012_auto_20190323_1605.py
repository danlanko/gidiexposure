# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-23 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0011_auto_20190323_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageslide',
            name='image',
            field=models.ImageField(help_text='Please upload images with dimension 1070 X 402 to get a balanced view', upload_to='home_slide'),
        ),
    ]
