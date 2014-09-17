# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20140907_1126'),
        ('sito', '0002_immagini'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('titolo_menu', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Menu:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('sliderev', models.BooleanField(default=False, help_text=b'Attiva su questa Gallery la Gallery Revolution', verbose_name=b'Gallery Revolution')),
                ('slidethumb', models.BooleanField(default=False, help_text=b'Attiva su questa pagina delle Miniature con pop up', verbose_name=b'Gallery Miniature')),
                (b'miniatura', image_cropping.fields.ImageRatioField(b'image', '500x281', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='miniatura')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '1200x675', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('categoria', models.ForeignKey(blank=True, to='sito.Categorie', null=True)),
                ('galleria', models.ManyToManyField(to='sito.Immagini', null=True, verbose_name=b'Seleziona Immagini Galleria', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Parole chiave')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo del Video:', blank=True)),
                ('youtubeurl', models.CharField(max_length=100, null=True, verbose_name=b'Indirizzo url youtube:', blank=True)),
                ('idyoutube', models.CharField(max_length=100, null=True, verbose_name=b'ID filmato:', blank=True)),
                ('start', models.IntegerField(default=0, null=True, verbose_name=b'Punto di Partenza del Filmato in secondi', blank=True)),
                ('embedded', models.TextField(null=True, verbose_name=b'Codice Embedded YouTube', blank=True)),
                ('thumb', models.ImageField(null=True, upload_to=b'uploaded_thum_youtube', blank=True)),
                ('link', models.CharField(max_length=100, null=True, blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Galleria Video',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(to='sito.Video', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name_plural': 'Categorie'},
        ),
    ]
