from django.db import models

# Create your models here.
class RentalProperty(models.Model):
    PROPERTY_TYPES = [
        ('residential', 'Residential'),
        ('penwell', 'Penwell'),
        ('airbnb', 'Airbnb'),
        ('commercial', 'Commercial')
    ]
    apt_number = models.CharField(max_length=20) 
    street_address = models.CharField(max_length=100, default='107 South 3rd Street West')  # Property address
    is_available = models.BooleanField(default=False)
    tenant_name = models.CharField(max_length=255, null=True, blank=True)
    tenant_phone = models.CharField(max_length=15, null=True, blank=True)
    bathrooms = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='Missoula')  
    state = models.CharField(max_length=10, default='MT')
    zip_code = models.CharField(max_length=10, default='59801')
    monthly_rent = models.IntegerField(max_length=10, default=0)
    property_type = models.CharField(
            max_length=20,
            choices=PROPERTY_TYPES,
            default='residential'  # Default to 'residential' to avoid migration issues
        )
    notes = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.apt_number