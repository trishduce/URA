from django.contrib import admin

from .models import RentalProperty


class RentalPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'apt_numb',
        'street_address',
        'city',
        'state',
        'zip_code',
        'is_available',
        'bathrooms',
        'tenant_name',
        'tenant_phone',
        'monthly_rent',
        'property_type',
        'notes',
    )
    
admin.site.register(RentalProperty, RentalPropertyAdmin) 