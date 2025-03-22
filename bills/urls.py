from django.urls import path
from .views import BillListView, BillDetailView

# Create your views here.
urlpatterns = [
    path('', BillListView.as_view(), name='bill_list'),
    path('<int:pk>/', BillDetailView.as_view(), name='bill_detail'),
]