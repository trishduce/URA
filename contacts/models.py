from django.db import models

class Contact(models.Model):
    business = models.CharField(max_length=255)
    bus_phone = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    cont_phone = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.business