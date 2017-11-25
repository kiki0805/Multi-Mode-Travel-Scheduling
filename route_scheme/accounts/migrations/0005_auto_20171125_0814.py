# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171125_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstatus',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location_count',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserStatus',
        ),
    ]
