# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_manager', '0002_auto_20171002_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crawelissue',
            old_name='user',
            new_name='created_by',
        ),
    ]
