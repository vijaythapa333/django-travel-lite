from django.contrib import admin
from .models import Group, Subscriber, Testimonials

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
	list_display = ('group_title', 'group_created_by')
	list_filter = ('group_created_at', )
	list_per_page = 10
	search_fields = ('group_title', 'group_description')


class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('subscriber_email', 'subscriber_first_name', 'subscriber_last_name', 'subscriber_contact')
	list_editable = ('subscriber_first_name', 'subscriber_last_name', 'subscriber_contact')
	list_filter = ('subscriber_created_at', )
	list_per_page = 10
	search_fields = ('subscriber_email', 'subscriber_first_name', 'subscriber_last_name', 'subscriber_contact')


class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('customer_name', 'customer_slug', 'customer_company', 'customer_job_title', 'testimonial_is_active', 'testimonial_is_featured')
	list_editable = ('customer_slug', 'customer_company', 'customer_job_title', 'testimonial_is_active', 'testimonial_is_featured')
	list_filter = ('testimonial_created_at', 'testimonial_is_active', 'testimonial_is_featured')
	list_per_page = 10
	search_fields = ('customer_name', 'customer_company')
	prepopulated_fields = {"customer_slug": ("customer_name", )}


admin.site.register(Group, GroupAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Testimonials, TestimonialAdmin)
