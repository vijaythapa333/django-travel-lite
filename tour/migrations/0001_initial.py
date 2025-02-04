# Generated by Django 2.2.4 on 2019-08-15 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(max_length=200, verbose_name='Activity Title')),
                ('activity_slug', models.SlugField(max_length=200, verbose_name='Activity Slug')),
                ('activity_description', models.TextField(blank=True, null=True, verbose_name='Activity Description')),
                ('activity_image', models.ImageField(blank=True, null=True, upload_to='activities/', verbose_name='Activity Image')),
                ('activity_icon', models.CharField(blank=True, max_length=200, null=True, verbose_name='Activity Icon')),
                ('activity_is_active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Active?')),
                ('activity_is_featured', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Featured?')),
                ('activity_created_at', models.DateTimeField(auto_now_add=True)),
                ('activity_update_at', models.DateTimeField(auto_now=True)),
                ('seo_activity_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='SEO Activity Title (60 Characters Long)')),
                ('seo_activity_keywords', models.TextField(blank=True, null=True, verbose_name='SEO Activity Keywords (Separated by Commas)')),
                ('seo_activity_description', models.TextField(blank=True, null=True, verbose_name='SEO Activity Description (160 Characters Long)')),
                ('activity_added_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
