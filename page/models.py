from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

POSITION = (
		('top', 'Top'),  			#Left for Value Right for Display
		('school', 'School'),
		('footer', 'Footer')
	)
IS_ACTIVE = (
		('yes', 'Yes'),
		('no', 'No')
	)


class Page(models.Model):
	page_title = models.CharField(max_length=200, verbose_name='Page Title')
	page_slug = models.SlugField(max_length=200, verbose_name='Page Slug')
	page_position = models.CharField(
			choices = POSITION,
			default='Top',
			max_length=20,
			verbose_name='Page Position'
		)
	page_description = RichTextField(blank=True, null=True, verbose_name="Page Description")
	page_image = models.ImageField(upload_to='pages/', blank=True, null=True, verbose_name="Page Image")
	page_is_active = models.CharField(
			choices = IS_ACTIVE,
			default='Yes',
			max_length=10,
			verbose_name='Is Active?'
		)
	page_is_featured = models.CharField(
			choices = IS_ACTIVE,
			default='Yes',
			max_length=10,
			verbose_name='Is Featured?'
		)
	page_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Page Created Date')
	page_updated_at = models.DateTimeField(auto_now=True, verbose_name='Page Updated Date')
	page_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Added By')

	# Meta for SEO
	seo_page_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="SEO Page Title (60 Characters Long)")
	seo_page_keywords = models.TextField(blank=True, null=True, verbose_name="SEO Page Keywords (Separated by Commas)")
	seo_page_description = models.TextField(blank=True, null=True, verbose_name="SEO Page Description (160 Characters Long)")


	def __str__(self):
		return self.page_title




