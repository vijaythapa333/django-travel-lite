from .models import Activity, Region, Tour



def head_menu(request):
	activity_menu = Activity.objects.filter(activity_is_active='yes')
	region_menu = Region.objects.filter(region_is_active='yes')
	context = {
		'activity_menu': activity_menu,
		'region_menu': region_menu
	}
	return context


def footer_tour_menu(request):
	best_tours = Tour.objects.filter(tour_is_active='yes', tour_is_featured='yes').order_by('-tour_created_at')[:5]
	popular_regions = Region.objects.filter(region_is_active='yes', region_is_featured='yes').order_by('-region_created_at')[:5]
	top_activities = Activity.objects.filter(activity_is_active='yes', activity_is_featured='yes').order_by('-activity_created_at')[:5]
	context = {
		'best_tours': best_tours,
		'popular_regions': popular_regions,
		'top_activities': top_activities
	}
	return context