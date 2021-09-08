import datetime as dt

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):   

    def __str__(self):
        return self.username

class Payment(models.Model):
    date = models.CharField(max_length=200)
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True)
    receiver = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True)
    sum = models.PositiveIntegerField()
    purpose = models.CharField(max_length=200)