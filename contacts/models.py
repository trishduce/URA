from django.db import models

class Contact(models.Model):
    business = models.CharField(max_length=255)
    bus_phone = models.CharField(max_length=20)
    contact = models.CharField(max_length=255)
    cont_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.business