# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-23 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0010_auto_20190323_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='home_slide')),
            ],
        ),
        migrations.RemoveField(
            model_name='homepageview',
            name='post',
        ),
        migrations.DeleteModel(
            name='HomePageView',
        ),
    ]
