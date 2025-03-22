from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy 
from .models import Maintenance

class MaintenanceListView(ListView):
  model = Maintenance
  template_name = 'maintenance_list.html'
  
class HomeView(ListView):
  model = Maintenance
  template_name = 'home.html'
  
class MaintenanceDetailView(DetailView):
  model = Maintenance
  template_name = 'maintenance_detail.html'
  
class MaintenanceUpdateView(UpdateView):
  model = Maintenance
  fields = (
    "urgency",
    "property",
    "pending",
    "description",
  )
  template_name = 'maintenance_edit.html'
  
class MaintenanceCreateView(CreateView):
  model = Maintenance
  fields = (
    "urgency",
    "property",
    "pending",
    "description",
  )
  template_name = 'maintenance_new.html'
  
  def get_success_url(self):
        return reverse_lazy('maintenance_list') 
  
class MaintenanceDeleteView(DeleteView):
  model = Maintenance
  template_name = 'maintenance_delete.html'
  success_url = reverse_lazy("maintenance_list")
