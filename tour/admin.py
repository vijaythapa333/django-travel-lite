from django.contrib import admin
from .models import Activity, Region, Tour



class ActivityAdmin(admin.ModelAdmin):
	list_display = ('activity_title', 'activity_slug', 'activity_is_active', 'activity_is_featured', 'activity_added_by')
	list_editable = ('activity_slug', 'activity_is_active', 'activity_is_featured')
	list_filter = ('activity_created_at', 'activity_is_active')
	list_per_page = 10
	search_fields = ('activity_title', 'activity_description')
	prepopulated_fields = {"activity_slug": ("activity_title", )}


class RegionAdmin(admin.ModelAdmin):
	list_display = ('region_title', 'region_slug', 'region_is_active', 'region_is_featured', 'region_added_by')
	list_editable = ('region_slug', 'region_is_active', 'region_is_featured')
	list_filter = ('region_created_at', 'region_is_active')
	list_per_page = 10
	search_fields = ('region_title', 'region_description')
	prepopulated_fields = {"region_slug": ("region_title", )}



class TourAdmin(admin.ModelAdmin):
	list_display = ('tour_title', 'tour_slug', 'tour_is_active', 'tour_is_featured', 'tour_added_by')
	list_editable = ('tour_slug', 'tour_is_active', 'tour_is_featured')
	list_per_page = 10
	list_filter = ('tour_created_at', 'tour_is_active')
	search_fields = ('tour_title', 'tour_description')
	prepopulated_fields = {"tour_slug": ("tour_title", )}


# Register your models here.
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Tour, TourAdmin)
