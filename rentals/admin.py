from django.contrib import admin

from .models import RentalProperty


class RentalPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'apt_number',
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
    )
    
admin.site.register(RentalProperty, RentalPropertyAdmin) 