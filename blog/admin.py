from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_title', 'category_slug', 'category_is_active')
	list_editable = ('category_slug', 'category_is_active')
	list_filter = ('category_is_active', 'category_created_at')
	list_per_page = 10
	search_fields = ('category_title', 'category_description')
	prepopulated_fields = {"category_slug": ("category_title", )}



class BlogAdmin(admin.ModelAdmin):
	list_display = ('blog_title', 'blog_slug', 'blog_is_active', 'blog_is_featured')
	list_editable = ('blog_slug', 'blog_is_active', 'blog_is_featured')
	list_filter = ('blog_created_at', 'blog_is_active')
	list_per_page = 10
	search_fields = ('blog_title', 'blog_description', 'seo_blog_keywords')
	prepopulated_fields = {"blog_slug": ("blog_title", )}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
