from django.contrib import admin
from django.urls import path, include
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
 	
 	path('', views.homePage, name="homePage"),
 	path('credits/', TemplateView.as_view(template_name = 'pages/credits.html'), name='creditsPage')
 	
]