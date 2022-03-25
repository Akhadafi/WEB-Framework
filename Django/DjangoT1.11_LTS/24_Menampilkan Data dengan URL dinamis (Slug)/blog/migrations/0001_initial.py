# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
    ]
