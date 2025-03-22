from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =  ("username", "email", "first_name", "last_name", "phone_number","profile_picture")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Deactivate user upon registration
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "phone_number","profile_picture")
