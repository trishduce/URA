# Create your models here.
from django.db import models

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    autopay = models.BooleanField(default=False)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.name