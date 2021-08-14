from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',null=True, blank=True)