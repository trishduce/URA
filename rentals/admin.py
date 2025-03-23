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
    list_display_links = ('name', 'apt_numb') 
    
admin.site.register(RentalProperty, RentalPropertyAdmin) 