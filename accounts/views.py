from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, DetailView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   template_name = "registration/signup.html"
   success_url = reverse_lazy("signup_success")  # Redirect to a success template
   
   def form_valid(self, form):
        print(self.request.FILES)
        form.instance.profile_picture = self.request.FILES.get('profile_picture')  # Handle file upload
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
   template_name = "registration/signup_success.html"

User = get_user_model()
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'  # Create this template
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user  # Display the profile of the logged-in user