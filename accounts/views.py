from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def settingsPage(request):
	return render (request, 'accounts/settings.html', locals())

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid():
				first_name = form.cleaned_data.get('first_name')
				form.save()
				messages.success(request, 'Bienvenue sur Beehave, ' + first_name + '! Veuillez vous connecter pour accéder à votre compte...')
				return redirect('loginPage')

	return render (request, 'accounts/register.html', locals())

def loginPage(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email = email, password = password)
		if user is not None:
			login(request, user)
			return redirect('settingsPage')
		else:
			messages.info(request, "Le mot de passe ou l'adresse mail fourni(e) est incorrect(e) ! Essayez à nouveau...")
	
	return render (request, 'accounts/login.html', locals())

def logoutUser(request):
	logout(request)
	return redirect('loginPage')