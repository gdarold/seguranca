from django.db import models

# Create your models here.
from django.urls import reverse


class Login(models.Model):
    nome = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    salto = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)
    permissions = models.CharField(max_length=20, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('logar_login')

    def __str__(self):
        return self.nome





