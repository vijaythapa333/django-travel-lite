from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from tour.models import Region, Activity, Tour
from blog.models import Blog
from marketing.forms import SubscribeForm
from marketing.models import Subscriber, Testimonials
from .models import Page
from django.contrib import messages

# Create your views here.



class HomePageView(TemplateView):
	# form_class = SubscribeForm
	# success_url ='/'
	# template_name = 'index.html'
	# For REquest Method
	def get(self, request, *args, **kwargs):
		regions = Region.objects.filter(region_is_active='yes', region_is_featured='yes').order_by('-region_created_at')[:3]
		activities = Activity.objects.filter(activity_is_active='yes', activity_is_featured='yes').order_by('-activity_created_at')[:6]
		tours = Tour.objects.filter(tour_is_active='yes', tour_is_featured='yes').order_by('-tour_created_at')[:10]
		featured_tours = Tour.objects.filter(tour_is_active='yes', tour_is_featured='yes').order_by('-tour_created_at')[:1]
		blogs = Blog.objects.filter(blog_is_active='yes', blog_is_featured='yes').order_by('-blog_created_at')[:3]
		testimonials = Testimonials.objects.filter(testimonial_is_active='yes', testimonial_is_featured='yes').order_by('-testimonial_created_at')[:3]

		context = {
			'regions': regions,
			'activities': activities,
			'tours': tours,
			'featured_tours': featured_tours,
			'blogs': blogs, 
			'testimonials': testimonials
		}
		return render(request, 'index.html', context)


	def post(self, request, *args, **kwargs):
		subscriber_email = request.POST["subscriber_email"]
		new_subscriber = Subscriber()
		new_subscriber.subscriber_email = subscriber_email
		new_subscriber.save()
		messages.success(self.request, 'Subscribed Successfully')
		return redirect('page:home')



class PageDetailView(DetailView):
	template_name = 'page/page_detail.html'
	model = Page
	slug_url_kwarg = 'page_slug'
	slug_field = 'page_slug'
	context_object_name = 'page'



class AboutPageView(TemplateView):
	template_name = 'about.html'



class BlogPageView(TemplateView):
	template_name = 'blog.html'



class ContactPageView(TemplateView):
	template_name = 'contact.html'


