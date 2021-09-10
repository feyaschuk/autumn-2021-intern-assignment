from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BalanceViewSet, RefillViewSet, TransferViewSet,
                    UserViewSet, WithdrawViewSet)

router_v1 = DefaultRouter(trailing_slash='optional')
router_v1.register('', UserViewSet, basename='users')
router_v1.register(r'(?P<user_id>\d+)/refill', RefillViewSet,
                   basename='refill')
router_v1.register(r'(?P<user_id>\d+)/withdraw', WithdrawViewSet,
                   basename='withdraw')
router_v1.register(r'(?P<user_id>\d+)/transfer', TransferViewSet,
                   basename='transfer')
router_v1.register(r'(?P<user_id>\d+)/balance', BalanceViewSet,
                   basename='balance')

urlpatterns = [
    path('users/', include(router_v1.urls)),
]
