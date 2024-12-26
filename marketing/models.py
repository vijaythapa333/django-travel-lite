from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Creating Choices instead of boolean for clear Usability
IS_ACTIVE = (
		('yes', 'Yes'), #Left for Value Right for Display
		('no', 'No')
	)


class Group(models.Model):
	group_title = models.CharField(max_length=100, verbose_name='Group Title')
	group_description = models.TextField(blank=True, null=True, verbose_name="Group Descritpion")
	group_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Created By')
	group_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Added Date")
	group_updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')


	def __str__(self):
		return self.group_title



class Subscriber(models.Model):
	subscriber_email = models.EmailField(max_length=100, verbose_name='Email Address')
	subscriber_first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='First Name')
	subscriber_last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Last Name')
	subscriber_contact = models.CharField(max_length=100, blank=True, null=True, verbose_name='Contact Number')
	subscriber_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='Group')
	subscriber_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added Date')
	subscriber_updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')


	def __str__(self):
		return self.subscriber_email


class Testimonials(models.Model):
	customer_name = models.CharField(max_length=100, verbose_name='Customer Name')
	customer_slug = models.SlugField(max_length=120, verbose_name='Customer Slug')
	customer_company = models.CharField(max_length=200, verbose_name='Customer Company')
	customer_job_title = models.CharField(max_length=100, verbose_name='Job Title')
	testimonial = models.TextField(verbose_name='Testimonial')
	testimonial_is_active = models.CharField(
		choices = IS_ACTIVE,
		default = 'Yes',
		max_length = 10,
		verbose_name = 'Is Active?'
	)
	testimonial_is_featured = models.CharField(
		choices=IS_ACTIVE,
		default='Yes',
		max_length=10,
		verbose_name='Is Featured?'
	)
	testimonial_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, verbose_name="Added By")
	testimonial_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
	testimonial_updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')


	def __str__(self):
		return self.customer_name
	