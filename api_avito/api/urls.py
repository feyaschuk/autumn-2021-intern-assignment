from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, RefillViewSet, BalanceViewSet, WithdrawViewSet, TransferViewSet)

router_v1 = DefaultRouter(trailing_slash='optional')
router_v1.register('users/?', UserViewSet, basename='users')
router_v1.register(r'users/(?P<user_id>\d+)/refill/?', RefillViewSet, basename='refill')
router_v1.register(r'users/(?P<user_id>\d+)/withdraw/?', WithdrawViewSet, basename='withdraw')
router_v1.register(r'users/(?P<user_id>\d+)/transfer/?', TransferViewSet, basename='transfer')
router_v1.register(
    r'users/(?P<user_id>\d+)/balance/?',
    BalanceViewSet, basename='balance')

urlpatterns = [    
    path('', include(router_v1.urls)),
]

