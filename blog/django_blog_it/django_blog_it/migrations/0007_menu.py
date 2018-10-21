# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0006_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('lvl', models.IntegerField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_blog_it.Menu')),
            ],
        ),
    ]
