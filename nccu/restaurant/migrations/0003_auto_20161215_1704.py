# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20161124_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='altitude',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='store',
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(to='restaurant.Restaurant'),
        ),
    ]
