from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def settingsPage(request):
	return render (request, 'accounts/settings.html', locals())

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid:
				form.save()
	return render (request, 'accounts/register.html', locals())