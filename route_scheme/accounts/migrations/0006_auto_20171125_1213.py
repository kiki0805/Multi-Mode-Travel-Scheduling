# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20171125_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='location_count',
            field=jsonfield.fields.JSONField(default={}, null=True, blank=True),
        ),
    ]
