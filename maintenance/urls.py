from django.urls import path
from .views import MaintenanceListView, MaintenanceDetailView, MaintenanceUpdateView, MaintenanceDeleteView, MaintenanceCreateView, HomeView


# Create your views here.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/maintenance/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('<int:pk>/', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('<int:pk>/edit/', MaintenanceUpdateView.as_view(), name='maintenance_edit'),
    path('/new/', MaintenanceCreateView.as_view(), name='maintenance_new'),
    path('<int:pk>/delete/', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
]