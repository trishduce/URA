from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'business',
        'bus_phone',
        'contact',
        'cont_phone',
    )
    
admin.site.register(Contact, ContactAdmin) 