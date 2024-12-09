from django.urls import path
from django.conf import settings #For Media
from django.conf.urls.static import static #For Media
from .views import BlogListView, BlogDetailView



app_name = 'blog'


urlpatterns = [
	path('all/', BlogListView.as_view(), name='all-blogs'),
	path('<slug:blog_slug>/', BlogDetailView.as_view(), name='blog-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)