# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0014_category_is_screen'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landscape1', models.ImageField(upload_to='advert')),
                ('landscape2', models.ImageField(upload_to='advert')),
                ('landscape3', models.ImageField(upload_to='advert')),
                ('square', models.ImageField(upload_to='advert')),
            ],
        ),
    ]
