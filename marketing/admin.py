from django.contrib import admin
from .models import Group, Subscriber

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



admin.site.register(Group, GroupAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
