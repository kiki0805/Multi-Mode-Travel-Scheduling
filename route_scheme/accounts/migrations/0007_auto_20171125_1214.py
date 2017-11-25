# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171125_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='modes',
            field=models.ManyToManyField(to='mode.Mode', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag', null=True, blank=True),
        ),
    ]
