from django.urls import path
from django.conf import settings #Needed for MEdia
from django.conf.urls.static import static # For MEdia
from .views import ActivityListView, RegionListView, TourListView, TourDetailView, RegionDetailView, ActivityDetailView



app_name = 'tour'


urlpatterns = [
	path('all/', TourListView.as_view(), name='all-tours'),
	path('activities/', ActivityListView.as_view(), name='all-activities'),
	path('activity/<slug:activity_slug>/', ActivityDetailView.as_view(), name='activity-detail'),
	path('regions/', RegionListView.as_view(), name='all-regions'),
	path('region/<slug:region_slug>/', RegionDetailView.as_view(), name='region-detail'),
	path('<slug:tour_slug>/', TourDetailView.as_view(), name='tour-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
