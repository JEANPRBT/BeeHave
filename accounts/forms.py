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
        fields = ('email', 'first_name','birthday', 'gender', 'wish_gender', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6','q7', 'q8', 'q9', 'q10')
        widgets = {
        'gender':Select(attrs={'class': 'input'}),
        'wish_gender':Select(attrs={'class': 'input'}),
        'email':EmailInput(attrs={'class':'input'}),
        'first_name':TextInput(attrs={'class': 'input'}),
        'birthday': DateInput(format=settings.DATE_INPUT_FORMATS, attrs={'class': 'input'}),
        'q1': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q2': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q3': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q4': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q5': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q6': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q7': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q8': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q9': NumberInput(attrs={'max':5, 'min':1,'class':'input'}),
        'q10': NumberInput(attrs={'max':5,'min':1,'class':'input'}),
        }

        def clean_birthday(self, *args, **kwargs):
            birthday = self.cleaned_data.get('birthday')
            birthdelta = (datetime.date.today()  - birthday)//datetime.timedelta(days=365.25)
            if birthdelta < 18 :
                raise forms.ValidationError("Vous devez être majeur pour continuer !")
            return birthday



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')


