from django.urls import path
from .views import ContactListView, ContactDetailView

# Create your views here.
urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
]