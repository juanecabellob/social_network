# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('todo_text', models.CharField(max_length=300)),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('progress', models.CharField(max_length=10)),
            ],
        ),
    ]
