from django.urls import path
from .views import SignUpView, SignUpSuccessView, ProfileView

urlpatterns = [
  path("signup/", SignUpView.as_view(), name="signup"),
  path("signup_success/", SignUpSuccessView.as_view(), name="signup_success"),
  path('profile/', ProfileView.as_view(), name='profile'),
]