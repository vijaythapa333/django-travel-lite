# Generated by Django 3.2.3 on 2024-12-20 06:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Page Description'),
        ),
    ]
