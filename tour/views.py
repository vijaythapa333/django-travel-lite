from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Tour, Region, Activity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class ActivityListView(View):
	# For List View
	# template_name = 'activity/all_activities.html'
	# model = Activity
	# context_object_name = 'activities'

	def get(self, request, *args, **kwargs):
		activities = Activity.objects.filter(activity_is_active='yes').order_by('-activity_created_at')
		recent_tours = Tour.objects.filter(tour_is_active='yes').order_by('-tour_created_at')[:3]
		context = {
			'activities': activities,
			'recent_tours': recent_tours
		}
		return render(request, 'activity/all_activities.html', context)


class ActivityDetailView(DetailView):
	template_name = 'activity/activity_detail.html'
	model = Activity
	slug_url_kwarg = 'activity_slug'
	slug_field = 'activity_slug'


	def get_context_data(self, **kwargs):
		activity = get_object_or_404(Activity, activity_slug=self.kwargs.get('activity_slug')) #Getting the current Activity by Activity Slug
		activity_tour_count = Tour.objects.filter(tour_activity=activity, tour_is_active='yes').count() #Count Tours by activity
		tours = Tour.objects.filter(tour_is_active='yes', tour_activity=activity).order_by('-tour_created_at') # Filtering the  Tours Based on Activity

		regions = Region.objects.filter(region_is_active='yes').order_by('-region_created_at')[:3]
		context = super().get_context_data(**kwargs)

		context['tours'] = tours
		context['activity_tour_count'] = activity_tour_count
		context['regions'] = regions
		return context



class RegionListView(ListView):
	template_name = 'region/all_regions.html'
	model = Region
	context_object_name = 'regions'
	paginate_by = 9



class RegionDetailView(DetailView):
	template_name = 'region/region_detail.html'
	model = Region
	slug_url_kwarg = 'region_slug'
	slug_field = 'region_slug'
	context_object_name = 'region'


	def get_context_data(self, **kwargs):
		region = get_object_or_404(Region, region_slug=self.kwargs.get('region_slug')) #Getting the Current Region by Region Slug
		tours = Tour.objects.filter(tour_is_active='yes', tour_region=region).order_by('-tour_created_at')
		region_tour_count = Tour.objects.filter(tour_region=region, tour_is_active='yes').count() #Counting Total Tours in Specific Region
		regions = Region.objects.filter(region_is_active='yes').exclude(region_slug=self.kwargs.get('region_slug')).order_by('-region_created_at')[:3]
		context = super().get_context_data(**kwargs)

		context['tours'] = tours
		context['region_tour_count'] = region_tour_count
		context['regions'] = regions
		return context


# Counting Tours based on Region




class TourListView(View):
	def get(self, request, *args, **kwargs):
		tour_list = Tour.objects.all().order_by('-tour_created_at')
		paginator = Paginator(tour_list, 6)
		page = request.GET.get('page')
		tours = paginator.get_page(page)

		regions = Region.objects.filter(region_is_active='yes', region_is_featured='yes').order_by('-region_created_at')[:3]
		context = {
			'tours': tours,
			'regions': regions
		}
		return render(request, 'tour/tour_list.html', context)


class TourDetailView(DetailView):
	template_name = 'tour/tour_detail.html'
	model = Tour
	slug_url_kwarg = 'tour_slug' #Slug name in URL
	slug_field = 'tour_slug' #SLug Column Name
	context_object_name = 'tour'


	def get_context_data(self, **kwargs):
		current_tour = get_object_or_404(Tour, tour_slug=self.kwargs.get('tour_slug'))
		#Displaying Similar Tours Based on Tour Region Excluding the Current Tour
		similar_tours = Tour.objects.filter(tour_is_active='yes', tour_region__in=current_tour.tour_region.all()).exclude(tour_slug=self.kwargs.get('tour_slug')).order_by('-tour_created_at')[:3]
		other_tours = Tour.objects.filter(tour_is_active='yes').order_by('-tour_created_at')[:3]
		regions = Region.objects.filter(region_is_active='yes').order_by('-region_created_at')[:3]
		context = super().get_context_data(**kwargs)

		context['similar_tours'] = similar_tours
		context['other_tours'] = other_tours
		context['regions'] = regions #Display Regions on Sidebar
		return context
