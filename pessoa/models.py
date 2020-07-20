from django.db import models
from seguranca.models import Login

class tipo_Person(models.Model):
    descricao = models.CharField(max_length=149)

    def __str__(self):
        return self.descricao

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(Login, null=False, blank=False, on_delete=models.PROTECT)
    age = models.IntegerField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='pessoa_fotos', null=True, blank=True)
    funcao = models.ForeignKey(tipo_Person,null=True, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.first_name



