# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_auto_20170823_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
