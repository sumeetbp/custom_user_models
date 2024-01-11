from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import django_filters

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['public_visibility']
