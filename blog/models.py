from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
IS_ACTIVE = (
		('yes', 'Yes'),
		('no', 'No')
	)




class Category(models.Model):
	category_title = models.CharField(max_length=200, verbose_name='Category Title')
	category_slug = models.SlugField(max_length=200, verbose_name='Category Slug')
	category_description = models.TextField(blank=True, null=True, verbose_name='Category Description')
	category_image = models.ImageField(upload_to='categories/', blank=True, null=True)
	category_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Active?'
		)
	category_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Category Created Date')
	category_updated_at = models.DateTimeField(auto_now=True, verbose_name='Category Updated Date')
	category_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Added By')

	# Meta for SEO
	seo_category_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='SEO Category Title (60 Characters Long)')
	seo_category_keywords = models.TextField(blank=True, null=True, verbose_name='SEO Category Keywords Separated by Commas')
	seo_category_description = models.TextField(blank=True, null=True, verbose_name='SEO Category Description (160 Characters Long)')


	def __str__(self):
		return self.category_title




class Blog(models.Model):
	blog_title = models.CharField(max_length=200, verbose_name='Blog Title')
	blog_slug = models.CharField(max_length=200, verbose_name='Blog Slug')
	blog_description = RichTextField(blank=True, null=True, verbose_name='Blog Description')
	blog_image = models.ImageField(upload_to='blogs/', blank=True, null=True, verbose_name='Blog Image')
	blog_category = models.ManyToManyField(Category, verbose_name='Blog Category')
	blog_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Active?'
		)
	blog_is_featured = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length = 10,
			verbose_name = 'Is Featured?'
		)
	blog_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Blog Created Date')
	blog_updated_at = models.DateTimeField(auto_now=True, verbose_name='Blog Updated Date')
	blog_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Added By')


	# Meta for SEO
	seo_blog_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='SEO Blog Title (60 Characters Long)')
	seo_blog_keywords = models.TextField(blank=True, null=True, verbose_name='SEO Blog Keywords (Separated by Commas)')
	seo_blog_description = models.TextField(blank=True, null=True, verbose_name='SEO Blog Description (160 Characters Long)')


	def __str__(self):
		return self.blog_title


	class Meta:
		ordering = ['-blog_created_at']

