# Create your models here.
from django.db import models

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    autopay = models.BooleanField(default=False)
    username = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name