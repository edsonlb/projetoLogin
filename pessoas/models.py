from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    endereco = models.CharField(max_length=100, blank=True, null=True)
