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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def average_O(self):
        o =(self.o1 + self.o2 + self.o3 + self.o4 + self.o5 + self.o6)/6
        return round(o, 1)


    def average_C(self):
        c =(self.c1 + self.c2 + self.c3 + self.c4 + self.c5 + self.c6)/6
        return round(c, 1)

    def average_E(self):
        e =(self.e1 + self.e2 + self.e3 + self.e4 + self.e5 + self.e6)/6
        return round(e, 1)

    def average_A(self):
        a =(self.a1 + self.a2 + self.a3 + self.a4 + self.a5 + self.a6)/6
        return round(a, 1)


    def average_N(self):
        n =(self.n1 + self.n2 + self.n3 + self.n4 + self.n5 + self.n6)/6
        return round(n, 1)
