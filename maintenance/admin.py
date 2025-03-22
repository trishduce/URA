from django.contrib import admin

from .models import Maintenance


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        'urgency',
        'property',
        'date_reported',
        'pending',
        'description',
    )
    
admin.site.register(Maintenance, MaintenanceAdmin) 