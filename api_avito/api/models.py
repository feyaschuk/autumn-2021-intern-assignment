import datetime as dt
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers, validators

CHOICES = [
    ('RUR', 'Rub'),
    ('USD', 'USD'),
    ('EUR', 'Euro'),]
OPERATIONS_CHOICES = [
    ('refill', 'refill account'),
    ('withdraw', 'withdraw account'),
    ('transfer', 'transfer to another account'),
    ('balance', 'check balance'),]
    
class User(AbstractUser):      
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
    sum =models.PositiveIntegerField()
    operation = models.CharField(max_length=25, choices = OPERATIONS_CHOICES)
    currency = models.CharField(max_length=3, choices = CHOICES, default='RUR')
    balance = models.IntegerField(blank=True,
        null=True)
 

class Balance(models.Model):  
    balance = models.PositiveIntegerField(blank=True,
        null=True) 
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='owner')
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3, choices = CHOICES, default='RUR')
    operation = models.CharField(max_length=25, choices = OPERATIONS_CHOICES)