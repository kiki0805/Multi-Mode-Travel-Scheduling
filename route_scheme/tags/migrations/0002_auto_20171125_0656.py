# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='related_tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
