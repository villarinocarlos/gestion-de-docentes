from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('docente', 'Docente'),
        ('coordinador', 'Coordinador'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='docente')
