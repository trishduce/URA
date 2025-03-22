from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from rentals.models import RentalProperty

class Maintenance(models.Model):

    URGENCY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='Medium')
    property = models.ForeignKey(RentalProperty, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)
    description = models.TextField(default='')


    def __str__(self):
        return f"{self.urgency} - {self.property} ({self.date_reported.strftime('%Y-%m-%d')})"
    
    def get_absolute_url(self):
        return reverse("maintenance_detail", kwargs={"pk": self.pk})
    
    

