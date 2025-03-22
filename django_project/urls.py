from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path("accounts/", include("django.contrib.auth.urls")), 
    path("", include("maintenance.urls")),
    path("rentals/", include("rentals.urls")),
    path("bills/", include("bills.urls")),
    path("contacts/", include("contacts.urls")),
    path("maintenance/", include("maintenance.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)