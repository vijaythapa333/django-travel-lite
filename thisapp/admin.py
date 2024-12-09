from django.contrib import admin
from .models import AppDetail, SocialMedia

# Register your models here.

class AppDetailAdmin(admin.ModelAdmin):
	list_display = ('app_name', 'app_title', 'app_email', 'app_contact', 'app_postal')
	list_editable = ('app_title', 'app_email', 'app_contact', 'app_postal')


class SocialMediaAdmin(admin.ModelAdmin):
	list_display = ('socialmedia_title', 'socialmedia_url', 'socialmedia_icon', 'socialmedia_is_active')
	list_editable = ('socialmedia_url', 'socialmedia_icon', 'socialmedia_is_active')



admin.site.register(AppDetail, AppDetailAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
