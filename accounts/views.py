from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

@login_required
def profilePage(request):
	email = request.user.email
	first_name = request.user.first_name
	wish_gender = request.user.wish_gender
	gender = request.user.gender
	return render (request, 'accounts/profile.html', locals())

def editProfile(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance = request.user)
		if form.is_valid : 
			form.save()
			return redirect('profilePage')
	else:
		form = CustomUserChangeForm(instance = request.user)
		return render(request, 'accounts/edit.html', locals())

def editPassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Votre nouveau mot de passe a bien été enregistré !')
			update_session_auth_hash(request, form.user)
			return redirect('profilePage')
		else:
			return redirect('editPassword')
	else:
		form = PasswordChangeForm(user = request.user)
	
	return render(request, 'accounts/editpassword.html', locals())					

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid():
				first_name = form.cleaned_data.get('first_name')
				form.save()
				subject= 'Thanks for signing up to Beehave !'
				message = 'Welcome to our great community at Beehave ! '
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
			return redirect('profilePage')
		else:
			messages.info(request, "Le mot de passe ou l'adresse mail fourni(e) est incorrect(e) ! Essayez à nouveau...")
	
	return render (request, 'accounts/login.html', locals())

def logoutUser(request):
	logout(request)
	return redirect('homePage')

