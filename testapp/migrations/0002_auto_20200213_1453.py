# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-02-13 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Eaddr',
            new_name='eaddr',
        ),
    ]
