# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0005_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('author', models.CharField(max_length=256, verbose_name='作者')),
                ('author_summary', models.TextField(verbose_name='作者简介')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('tags', models.CharField(max_length=50, verbose_name='标签')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
    ]
