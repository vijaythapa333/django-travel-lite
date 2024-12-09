from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('page_title', 'page_slug', 'page_position', 'page_is_active', 'page_is_featured')
	list_editable = ('page_slug', 'page_position', 'page_is_active', 'page_is_featured')
	list_filter = ('page_position', 'page_is_active', 'page_is_featured')
	list_per_page=10
	search_fields = ('page_title', 'page_description')
	prepopulated_fields = {"page_slug": ("page_title", )}



admin.site.register(Page, PageAdmin)
