# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_miniurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name=b'Nom')),
                ('prenom', models.CharField(max_length=60, verbose_name=b'Prenom')),
            ],
        ),
    ]
