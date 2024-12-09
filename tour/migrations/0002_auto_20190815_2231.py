# Generated by Django 2.2.4 on 2019-08-15 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_added_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Added By'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_title', models.CharField(max_length=200, verbose_name='Region Title')),
                ('region_slug', models.CharField(max_length=200, verbose_name='Region Slug')),
                ('region_description', models.TextField(blank=True, null=True, verbose_name='Region Description')),
                ('region_image', models.ImageField(blank=True, null=True, upload_to='regions/', verbose_name='Region Image')),
                ('region_is_active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Active?')),
                ('region_is_featured', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Featured?')),
                ('region_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('region_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('seo_region_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Region Title (60 Characters Long)')),
                ('seo_region_keywords', models.TextField(blank=True, null=True, verbose_name='SEO Region Keywords (Separated by Commas)')),
                ('seo_region_description', models.TextField(blank=True, null=True, verbose_name='SEO Region Description (160 Characters Long)')),
                ('region_added_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
            ],
        ),
    ]