from django.db import models
from django.contrib.auth.models import User

# Create your models here.
IS_ACTIVE = (
		('yes', 'Yes'),
		('no', 'No')
	)



class AppDetail(models.Model):
	app_name = models.CharField(max_length=200, verbose_name="Website Name")
	app_title = models.CharField(max_length=200, verbose_name="Website Title (60 Characters Long)")
	app_logo = models.ImageField(blank=True, null=True, verbose_name="Website Logo")
	app_icon = models.ImageField(blank=True, null=True, verbose_name="Website Favicon")
	app_keywords = models.TextField(blank=True, null=True, verbose_name="Website Keywords (Separated by Commas)")
	app_description = models.TextField(blank=True, null=True, verbose_name="Website Description (160 Characters Long)")
	app_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Primary Email for Website")
	app_contact = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contact Number for Website", help_text="Please add country code with contact number but no spaces.")
	app_address = models.TextField(blank=True, null=True, verbose_name="Physical Address for the Website")
	app_postal = models.CharField(max_length=10, blank=True, null=True, verbose_name="Postal Address for the Website")
	whatsapp_booking = models.CharField(
		choices=IS_ACTIVE,
		default='Yes',
		max_length=10,
		verbose_name='Book On Whatsapp?',
		help_text='Select Yes to accept booking on WhatsApp. Also make sure Contact Number is added.'
	)
	developed_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Developed By", help_text='Do not change it. Changing it may cause your website to not function correctly.')
	app_created_at = models.DateTimeField(auto_now_add=True, verbose_name="App Created Date")
	app_updated_at = models.DateTimeField(auto_now=True, verbose_name="App Updated Date")


	def __str__(self):
		return self.app_name



class SocialMedia(models.Model):
	socialmedia_title = models.CharField(max_length=20, verbose_name="Social Media Name")
	socialmedia_url = models.URLField(max_length=150, verbose_name="Social Media URL")
	socialmedia_icon = models.CharField(max_length=200, blank=True, null=True, verbose_name="Social Media Icon")
	socialmedia_is_active = models.CharField(
			choices = IS_ACTIVE,
			default = 'Yes',
			max_length=10,
			verbose_name='Is Active?'
		)
	socialmedia_craeted_at = models.DateTimeField(auto_now_add=True, verbose_name="Social Media Created Date")
	socialmedia_updated_at = models.DateTimeField(auto_now=True, verbose_name="Social Media Updated Date")
	socialmedia_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Social Media Added By")


	def __str__(self):
		return self.socialmedia_title
