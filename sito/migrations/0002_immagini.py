# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immagini',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x480', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slider', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slider')),
                (b'thumb', image_cropping.fields.ImageRatioField(b'image', '595x335', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='thumb')),
                (b'croppinguno', image_cropping.fields.ImageRatioField(b'image', '1140x487', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppinguno')),
                (b'croppingdue', image_cropping.fields.ImageRatioField(b'image', '198x132', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingdue')),
                (b'croppingtre', image_cropping.fields.ImageRatioField(b'image', '1199x674', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingtre')),
                (b'croppingquattro', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design Miniatura')),
                (b'croppingcinque', image_cropping.fields.ImageRatioField(b'image', '1200x800', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Design HD')),
                (b'croppingsei', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'News')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Galleria Immagini',
            },
            bases=(models.Model,),
        ),
    ]
