from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators

from .models import User, Payment, Balance
from .serializers import UserSerializer, RefillSerializer, BalanceSerializer, WithdrawSerializer,TransferSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RefillViewSet(viewsets.ModelViewSet):    
    serializer_class = RefillSerializer
    
    def perform_create(self, serializer):                            
        sender= User.objects.get(id=self.kwargs.get("user_id"))                 
        sum = self.request.data['sum']
        if len(list(Balance.objects.filter(owner=sender))) > 0:
            current_balance = list(Balance.objects.filter(owner=sender))[-1].balance
        else:
            current_balance = 0
        balance = current_balance + sum
        Balance.objects.create(owner=sender, operation ='refill', balance=balance)
        return serializer.save(sender=sender, receiver = sender,
                               operation ='refill', balance=balance)

    def get_queryset(self):
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        payment = Payment.objects.filter(sender=sender, operation ='refill')
        return payment.all()    
    
class WithdrawViewSet(viewsets.ModelViewSet):    
    serializer_class = WithdrawSerializer

    def perform_create(self, serializer):                            
        sender= User.objects.get(id=self.kwargs.get("user_id"))                 
        sum = self.request.data['sum']
        if len(list(Balance.objects.filter(owner=sender))) > 0:
            current_balance = list(Balance.objects.filter(owner=sender))[-1].balance
        else:
            current_balance = 0        
        balance = current_balance - sum
        if balance<=0:
            raise validators.ValidationError('Недостаточно средств на счете.')
        Balance.objects.create(owner=sender, operation ='withdraw', balance=balance)
        return serializer.save(sender=sender, receiver = sender,
                               operation ='withdraw', balance=balance)

    def get_queryset(self):
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        payment = Payment.objects.filter(sender=sender, operation ='withdraw')
        return payment.all()   
  
    
class TransferViewSet(viewsets.ModelViewSet):    
    serializer_class = TransferSerializer

    def perform_create(self, serializer):                            
        sender= User.objects.get(id=self.kwargs.get("user_id"))
        try:
            receiver= User.objects.get(id=self.request.data['receiver'])
        except:
            raise validators.ValidationError("Получателя не существует, проверьте номер получателя.")
        try:
            sender==receiver
        except:
            raise validators.ValidationError('Получатель и отправитель совпадают, проверьте номер получателя.')                
        sum = self.request.data['sum']
        if len(list(Balance.objects.filter(owner=sender))) > 0:
            current_balance = list(Balance.objects.filter(owner=sender))[-1].balance
        else:
            current_balance = 0 
        if len(list(Balance.objects.filter(owner=receiver))) > 0:
            reciver_balance = list(Balance.objects.filter(owner=receiver))[-1].balance
        else:
            reciver_balance = 0 
        balance = current_balance - sum
        if balance<=0:
            raise validators.ValidationError('Недостаточно средств на счете.')
        Balance.objects.create(owner=sender, operation =f'transfer to {receiver}', balance=balance)
        Balance.objects.create(owner=receiver, operation =f'transfer from {sender}', 
                               balance=(reciver_balance + sum))
        return serializer.save(sender=sender, receiver = sender,
                               operation ='transfer', balance=balance)
         
        
    def get_queryset(self):
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        payment = Payment.objects.filter(sender=sender, operation ='transfer')
        return payment.all()      


class BalanceViewSet(viewsets.ModelViewSet):      
    serializer_class = BalanceSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('created', 'balance', )
            
    def get_queryset(self):
        owner = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return Balance.objects.filter(owner=owner).order_by('-created')    

    
 

    



