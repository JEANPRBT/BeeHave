from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import CustomUser, UserAnswers


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'gender', 'wish_gender')

class UserAnswersForm(ModelForm):
	class Meta :
		model = UserAnswers
		fields = ('__all__')
