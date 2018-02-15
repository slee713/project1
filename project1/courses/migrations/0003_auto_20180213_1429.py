# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_steps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Step',
        ),
    ]
