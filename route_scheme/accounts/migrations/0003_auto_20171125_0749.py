# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_modes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstatus',
            name='count',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='location',
        ),
        migrations.AddField(
            model_name='userstatus',
            name='location_count',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
    ]
