# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashuser',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
