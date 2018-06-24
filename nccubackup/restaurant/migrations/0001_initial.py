# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('opentime', models.CharField(max_length=50, blank=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('menu', models.ImageField(upload_to='C:\\Users\\user\\Envs\\nccu\\nccu\\menupic')),
                ('store', models.ImageField(upload_to='C:\\Users\\user\\Envs\\nccu\\nccu\\storepic')),
            ],
        ),
    ]
