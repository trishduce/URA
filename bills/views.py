from django.views.generic import ListView, DetailView
from .models import Bill

class BillListView(ListView):
  model = Bill
  template_name = 'bill_list.html'
  
class BillDetailView(DetailView):
  model = Bill
  template_name = 'bill_detail.html'
  
