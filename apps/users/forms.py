from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'customer')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'customer')
        widgets = {'customer': forms.TextInput(attrs={'class': 'form-control'}),}
