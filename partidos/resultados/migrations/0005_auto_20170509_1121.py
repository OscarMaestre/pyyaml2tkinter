# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0004_victorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='victorias',
            name='derrotas_totales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='victorias',
            name='empates_totales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='victorias',
            name='victorias_totales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
