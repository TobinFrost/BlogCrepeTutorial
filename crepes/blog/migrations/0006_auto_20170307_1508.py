# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_personne_nb_modif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='nb_modif',
            field=models.IntegerField(null=True, verbose_name=b'Nombre de Modification'),
        ),
    ]
