# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0005_auto_20170509_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='victorias',
            old_name='nombre',
            new_name='equipo',
        ),
    ]