# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anticounterfeit', '0014_auto_20151207_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'%y%m%d'),
        ),
    ]
