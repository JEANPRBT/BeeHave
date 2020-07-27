from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CustomUserManager
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [('Homme', 'Un homme'), ('Femme', 'Une femme')]
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES, default = 'Homme')
    wish_gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default = 'Femme')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

def questions_time():
        return timezone.now() - timezone.timedelta(seconds = 5)

class UserAnswers(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, default = CustomUser.objects.get(date_joined__gt = questions_time()))
    q1 = models.PositiveIntegerField()
    s1 = models.PositiveIntegerField()

    def __str__(self):
        return self.user.email



 