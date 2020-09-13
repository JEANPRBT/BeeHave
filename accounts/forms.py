from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from datetime import datetime
from django.forms.widgets import PasswordInput, TextInput, NumberInput, DateInput, EmailInput, Select
from django.forms import ModelForm
from .models import CustomUser
from beehave import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','birthday', 'gender', 'wish_gender', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6','c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6')
        widgets = {
        'gender':Select(attrs={'class': 'gender'}),
        'wish_gender':Select(attrs={'class': 'wish_gender'}),
        'email':EmailInput(attrs={'class':'email'}),
        'first_name':TextInput(attrs={'class': 'first_name'}),
        'birthday': DateInput(format=settings.DATE_INPUT_FORMATS, attrs={'class': 'birthday', 'type': 'date'}),
        'o1': NumberInput(attrs={'max':5, 'min':1}),
        'o2': NumberInput(attrs={'max':5, 'min':1}),
        'o3': NumberInput(attrs={'max':5, 'min':1}),
        'o4': NumberInput(attrs={'max':5, 'min':1}),
        'o5': NumberInput(attrs={'max':5, 'min':1}),
        'o6': NumberInput(attrs={'max':5, 'min':1}),
        'c1': NumberInput(attrs={'max':5, 'min':1}),
        'c2': NumberInput(attrs={'max':5, 'min':1}),
        'c3': NumberInput(attrs={'max':5, 'min':1}),
        'c4': NumberInput(attrs={'max':5, 'min':1}),
        'c5': NumberInput(attrs={'max':5, 'min':1}),
        'c6': NumberInput(attrs={'max':5, 'min':1}),
        'e1': NumberInput(attrs={'max':5, 'min':1}),
        'e2': NumberInput(attrs={'max':5, 'min':1}),
        'e3': NumberInput(attrs={'max':5, 'min':1}),
        'e4': NumberInput(attrs={'max':5, 'min':1}),
        'e5': NumberInput(attrs={'max':5, 'min':1}),
        'e6': NumberInput(attrs={'max':5, 'min':1}),
        'a1': NumberInput(attrs={'max':5, 'min':1}),
        'a2': NumberInput(attrs={'max':5, 'min':1}),
        'a3': NumberInput(attrs={'max':5, 'min':1}),
        'a4': NumberInput(attrs={'max':5, 'min':1}),
        'a5': NumberInput(attrs={'max':5, 'min':1}),
        'a6': NumberInput(attrs={'max':5, 'min':1}),
        'n1': NumberInput(attrs={'max':5, 'min':1}),
        'n2': NumberInput(attrs={'max':5, 'min':1}),
        'n3': NumberInput(attrs={'max':5, 'min':1}),
        'n4': NumberInput(attrs={'max':5, 'min':1}),
        'n5': NumberInput(attrs={'max':5, 'min':1}),
        'n6': NumberInput(attrs={'max':5, 'min':1}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')

        widgets = {
        'email':EmailInput(attrs = {'class':'input'}),
        'first_name':TextInput(attrs = {'class':'input'}),
        'gender':Select(attrs = {'class':'input'}),
        'wish_gender':Select(attrs = {'class':'input'}),
        }


