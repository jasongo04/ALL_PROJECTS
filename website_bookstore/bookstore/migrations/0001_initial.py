# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-26 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=50, verbose_name='书名')),
                ('pub_house', models.CharField(default='', max_length=100, verbose_name='出版社')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='定价')),
                ('market_price', models.DecimalField(decimal_places=2, default=9999, max_digits=7, verbose_name='零售价')),
            ],
        ),
    ]
