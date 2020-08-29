from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [('Homme', 'Un homme'), ('Femme', 'Une femme')]
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES, default = 'Homme')
    wish_gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default = 'Femme')
    q1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q7 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q8 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q9 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    q10 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email





 