# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20170126_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='fb_link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='store',
            field=models.ImageField(upload_to='/home/sg35/virtualenvs/NccuMap/nccu/store'),
        ),
    ]
