# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100)),
                ('sottotitolo', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
