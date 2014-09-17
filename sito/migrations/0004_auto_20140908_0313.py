# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0003_auto_20140907_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name=b'miniatura',
            field=image_cropping.fields.ImageRatioField(b'image', '960x1280', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='miniatura'),
        ),
    ]
