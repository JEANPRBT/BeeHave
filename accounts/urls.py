from django.urls import path, include
from . import views

urlpatterns = [

path('', views.settingsPage, name = 'settingsPage'),
path('register/', views.registerPage, name = 'registerPage'),
path('login/', views.loginPage, name = "loginPage"),
path('logout/', views.logoutUser, name = 'logoutUser')

]