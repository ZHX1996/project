# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(db_index=True, verbose_name='网址', max_length=256)),
                ('content', models.TextField(verbose_name='内容', blank=True, default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='作者', null=True)),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(db_index=True, verbose_name='栏目网址', max_length=256)),
                ('intro', models.TextField(verbose_name='栏目介绍', default='')),
            ],
            options={
                'verbose_name_plural': '栏目',
                'verbose_name': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='app.Column', verbose_name='归属栏目'),
        ),
    ]
