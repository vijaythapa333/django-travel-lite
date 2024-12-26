# Generated by Django 3.2.3 on 2024-12-26 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0002_auto_20190823_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, verbose_name='Customer Name')),
                ('customer_slug', models.SlugField(max_length=120, verbose_name='Customer Slug')),
                ('customer_company', models.CharField(max_length=200, verbose_name='Customer Company')),
                ('customer_job_title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('testimonial', models.TextField(verbose_name='Testimonial')),
                ('testimonial_is_active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Active?')),
                ('testimonial_is_featured', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=10, verbose_name='Is Featured?')),
                ('testimonial_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('testimonial_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('testimonial_added_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
            ],
        ),
    ]
