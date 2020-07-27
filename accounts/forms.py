from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender', 'q1', 's1')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')


