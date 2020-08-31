from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from datetime import datetime
from django.db.models.expressions import F
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
    o1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    o2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    o3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    o4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    o5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    o6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    c6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    e6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    a6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n1 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n2 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n3 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n4 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n5 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])
    n6 = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])

    average_o = (F('o1') + F('o2') + F('o3') + F('o4') + F('o5') + F('o6'))/6

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    



 