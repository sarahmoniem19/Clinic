# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClinic', '0003_hospital_lab_labanalysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
