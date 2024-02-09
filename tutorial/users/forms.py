from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.forms import ModelForm 



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']