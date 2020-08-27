from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput, NumberInput
from django.forms import ModelForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender', 'q1', 's1')
        widgets = {
        'q1': NumberInput(attrs={'max':10}),
        's1': NumberInput(attrs={'max':10})
        }



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')


