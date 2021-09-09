from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import User, Payment
from .serializers import UserSerializer, RefillSerializer, BalanceSerializer, WithdrawSerializer,TransferSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class RefillViewSet(viewsets.ModelViewSet):    
    serializer_class = RefillSerializer
    
    def perform_create(self, serializer):
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return serializer.save()

    def get_queryset(self):
        payment = Payment.objects.all()
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return payment.all()    
    
    

class WithdrawViewSet(viewsets.ModelViewSet):    
    serializer_class = WithdrawSerializer
    def perform_create(self, serializer):
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return serializer.save()

    def get_queryset(self):
        payment = Payment.objects.all()
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return payment.all()  
  

    
class TransferViewSet(viewsets.ModelViewSet):    
    serializer_class = TransferSerializer

    def perform_create(self, serializer):        
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        a = self.request.data['sender']
        sender= User.objects.get(id=self.request.data['sender'])
        receiver = User.objects.get(id=self.request.data['receiver'])
        return serializer.save(sender=sender, receiver=receiver)
        

    def get_queryset(self):
        payment = Payment.objects.all()
        sender = get_object_or_404(User, pk=self.kwargs.get("user_id"))
        return payment.all()  


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

    



