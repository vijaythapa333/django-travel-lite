# Generated by Django 2.2.4 on 2019-08-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190820_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-blog_created_at']},
        ),
    ]
