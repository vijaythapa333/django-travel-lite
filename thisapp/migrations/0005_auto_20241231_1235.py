# Generated by Django 3.2.3 on 2024-12-31 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thisapp', '0004_appdetail_app_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdetail',
            name='app_icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Website Favicon'),
        ),
        migrations.AddField(
            model_name='appdetail',
            name='developed_by',
            field=models.CharField(blank=True, help_text='Do not change it. Changing it may cause cause your website to not function correctly.', max_length=20, null=True, verbose_name='Developed By'),
        ),
        migrations.AddField(
            model_name='appdetail',
            name='whatsapp_booking',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', help_text='Select Yes to accept booking on WhatsApp.', max_length=10, verbose_name='Book On Whatsapp?'),
        ),
    ]
