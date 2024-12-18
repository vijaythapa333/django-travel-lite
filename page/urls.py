from django.urls import path
from django.conf import settings #Needed for MEdia
from django.conf.urls.static import static # For MEdia
from .views import HomePageView, BlogPageView, ContactPageView, PageDetailView



app_name = 'page'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('<slug:page_slug>/', PageDetailView.as_view(), name='page-detail'),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
