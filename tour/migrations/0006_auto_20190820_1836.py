# Generated by Django 2.2.4 on 2019-08-20 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_auto_20190815_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['-region_created_at']},
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='activity_update_at',
            new_name='activity_updated_at',
        ),
    ]
