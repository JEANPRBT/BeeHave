from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [('Homme', 'Un homme'), ('Femme', 'Une femme')]
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES, default = 'Homme')
    wish_gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default = 'Femme')
    q1 = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
        ])
    s1 = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
        ])



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email





 