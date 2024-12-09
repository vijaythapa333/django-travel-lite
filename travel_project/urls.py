
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('tour/', include('tour.urls')),
    path('blog/', include('blog.urls')),
    path('marketing/', include('marketing.urls')),
]


# Customizing Admin Panel Texts
admin.site.site_header = 'Django Travel Project'
admin.site.index_title = 'Manage Travels'
admin.site.site_title = 'Travel Site | Control Panel'