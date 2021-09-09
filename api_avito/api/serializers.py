from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, validators
from django.shortcuts import get_object_or_404
from rest_framework.relations import StringRelatedField

from .models import User, Payment

#class MyModelSerializer(QueryFieldsMixin, ModelSerializer):
    #include_arg_name = 'show'
    #exclude_arg_name = 'exclude'
    #pass
class BalanceSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id','balance',)

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',            
            'balance', )

class RefillSerializer(ModelSerializer):
    sender_balance = serializers.SerializerMethodField()   

    class Meta:
        model = Payment
        fields = '__all__'    

    def get_sender_balance(self, obj):        
        payment = Payment.objects.get(id=obj.id)  
        sum = obj.sum 
        balance = payment.sender.balance + sum
        return balance

    

class WithdrawSerializer(ModelSerializer):
    sender_balance = serializers.SerializerMethodField()   

    class Meta:
        model = Payment
        fields = '__all__'

    def get_sender_balance(self, obj):        
        payment = Payment.objects.get(id=obj.id)  
        sum = obj.sum 
        balance = payment.sender.balance - sum
        return balance

class TransferSerializer(ModelSerializer):
    sender_balance = serializers.SerializerMethodField() 
    receiver_balance  = serializers.SerializerMethodField() 
    sender = StringRelatedField(read_only=True)
    receiver = StringRelatedField(read_only=True)
    

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('sender', 'receiver')

    def get_sender_balance(self, obj):        
        payment = Payment.objects.get(id=obj.id)  
        sum = obj.sum 
        balance = payment.sender.balance - sum        
        return balance

    def get_receiver_balance(self, obj):        
        payment = Payment.objects.get(id=obj.id)  
        sum = obj.sum         
        balance = payment.receiver.balance + sum
        return balance