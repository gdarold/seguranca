from django.db import models

# Create your models here.


class Login(models.Model):
    login = models.CharField(max_length=50)
    password = models.TextField()
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.login


objectos = models.Manager()

