# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20171125_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='related_tags',
            field=models.ManyToManyField(related_name='related_tags_rel_+', to='tags.Tag', blank=True),
        ),
    ]
