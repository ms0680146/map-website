# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20161215_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('store', models.ImageField(upload_to='C:\\Users\\user\\Envs\\nccu\\nccu\\store')),
                ('storename', models.ForeignKey(to='restaurant.Restaurant')),
            ],
        ),
    ]
