from django.contrib import admin

from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'website',
        'account_number',
        'autopay',
        'username',
    )
    
admin.site.register(Bill, BillAdmin) 