from django.db import models

# Create your models here.
class RentalProperty(models.Model):
    PROPERTY_TYPES = [
        ('residential', 'Residential'),
        ('penwell', 'Penwell'),
        ('airbnb', 'Airbnb'),
        ('commercial', 'Commercial')
    ]
    name = models.CharField(max_length=30, null=True, blank=True) 
    apt_number = models.IntegerField(default=0)   
    street_address = models.CharField(max_length=100, default='107 South 3rd Street West')  # Property address
    is_available = models.BooleanField(default=False)
    tenant_name = models.CharField(max_length=255, null=True, blank=True)
    tenant_phone = models.CharField(max_length=15, null=True, blank=True)
    bathrooms = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='Missoula')  
    state = models.CharField(max_length=10, default='MT')
    zip_code = models.CharField(max_length=10, default='59801')
    monthly_rent = models.IntegerField(default=0)
    property_type = models.CharField(
            max_length=20,
            choices=PROPERTY_TYPES,
            default='residential'  # Default to 'residential' to avoid migration issues
        )
    notes = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        if int(self.apt_number) > 0:
            return str(self.apt_number)
        else:
            return self.name