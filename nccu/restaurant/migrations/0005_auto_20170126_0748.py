# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='store',
            field=models.ImageField(upload_to='/home/sg35/virtualenvs/python3/nccu/nccu/store'),
        ),
    ]
