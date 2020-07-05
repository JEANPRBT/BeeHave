from django.shortcuts import render
from accounts import views 

# Create your views here.

def homePage(request):
	"""Page d'accueil du site"""
	return render(request, 'pages/home.html', locals())