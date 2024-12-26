from django.urls import path
from .views import TestimonialListView


app_name = 'marketing'


urlpatterns = [
	path('testimonials/', TestimonialListView.as_view(), name='all-testimonials'),
]