from django.shortcuts import render
from django.views.generic import View
from .models import Testimonials
from tour.models import Tour

# Create your views here.

class TestimonialListView(View):
    def get(self, request, *args, **kwargs):
        testimonials = Testimonials.objects.filter(testimonial_is_active='yes').order_by('-testimonial_created_at')
        featured_tours = Tour.objects.filter(tour_is_active='yes', tour_is_featured='yes').order_by('-tour_created_at')[:6]
        context = {
            'testimonials': testimonials,
            'featured_tours': featured_tours
        }
        return render(request, 'marketing/all_testimonials.html', context)
