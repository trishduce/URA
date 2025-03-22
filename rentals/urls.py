from django.urls import path
from .views import ResidentialListView, PenwellListView, ResidentialDetailView, PenwellDetailView


urlpatterns = [
    path('residential/', ResidentialListView.as_view(), name='residential_list'),
    path('penwell/', PenwellListView.as_view(), name='penwell_list'),
    path('penwell/<int:pk>/', PenwellDetailView.as_view(), name='penwell_detail'),  
    path('residential/<int:pk>/', ResidentialDetailView.as_view(), name='residential_detail'), 
]
