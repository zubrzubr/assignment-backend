# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_tasks', to='board.Board')),
            ],
        ),
    ]
