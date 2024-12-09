from django.urls import path
from django.conf import settings #Needed for MEdia
from django.conf.urls.static import static # For MEdia
from .views import HomePageView, BlogPageView, ContactPageView, CarPageView, FlightPageView, HotelPageView, VacationPageView, PageDetailView



app_name = 'page'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:page_slug>/', PageDetailView.as_view(), name='page-detail'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('car/', CarPageView.as_view(), name='car'),
    path('flight/', FlightPageView.as_view(), name='flight'),
    path('hotel/', HotelPageView.as_view(), name='hotel'),
    path('vacation/', VacationPageView.as_view(), name='vacation'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
