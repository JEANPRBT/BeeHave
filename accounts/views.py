from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

# Create your views here.

@login_required
def settingsPage(request):
	return render (request, 'accounts/settings.html', locals())

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid():
				first_name = form.cleaned_data.get('first_name')
				form.save()
				subject= 'Thanks for signing up to Beehave !'
				message = 'Welcome to our great community at Beehave ! \n Please click on the link below to confirm.'
				from_email = settings.EMAIL_HOST_USER
				mail_to = [form.cleaned_data.get('email'), settings.EMAIL_HOST_USER]
				send_mail(subject, message, from_email, mail_to, fail_silently = False)

				messages.success(request, 'Bienvenue sur Beehave, ' + first_name + ' !')
				messages.success(request, 'Vos réponses ont bien été enregistrées, veuillez vous connecter pour accéder à votre compte...')

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

