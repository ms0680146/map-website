# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='altitude',
            field=models.FloatField(null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=models.ImageField(null=True, upload_to='C:\\Users\\user\\Envs\\nccu\\nccu\\menupic', blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opentime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='store',
            field=models.ImageField(null=True, upload_to='C:\\Users\\user\\Envs\\nccu\\nccu\\storepic', blank=True),
        ),
    ]
