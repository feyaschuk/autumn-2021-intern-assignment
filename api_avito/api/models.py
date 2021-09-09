import datetime as dt

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):   
    balance = models.PositiveIntegerField() 
    def __str__(self):
        return self.username

class Payment(models.Model):
    date = models.DateTimeField('Дата добавления', auto_now_add=True, db_index=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='receiver')
    sum = models.PositiveIntegerField()
    purpose = models.CharField(max_length=200, blank=True,
        null=True)
    currency = models.CharField(max_length=3, default='RUR')