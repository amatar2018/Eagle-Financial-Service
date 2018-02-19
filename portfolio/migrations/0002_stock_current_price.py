# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='current_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]