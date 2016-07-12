# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20160709_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=50, verbose_name='\u53d1\u5e03\u4eba')),
                ('contente', models.TextField(verbose_name='\u53d1\u5e03\u5185\u5bb9')),
                ('infoTime', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
        ),
    ]