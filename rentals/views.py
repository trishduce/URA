from django.views.generic import ListView, DetailView
from .models import RentalProperty

class ResidentialListView(ListView):
  model = RentalProperty
  template_name = "residentialrentals.html"
  ordering = ['name']
  
class PenwellListView(ListView):
  model = RentalProperty
  template_name = "penwellrentals.html"
  ordering = ['apt_numb']
  
class ResidentialDetailView(DetailView):
  model = RentalProperty
  template_name = "residentialdetail.html"
  
class PenwellDetailView(DetailView):
  model = RentalProperty
  template_name = "penwelldetail.html"