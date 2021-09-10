from drf_queryfields import QueryFieldsMixin
from rest_framework import validators
from rest_framework.serializers import ModelSerializer

from .models import Balance, Payment, User


class MyModelSerializer(QueryFieldsMixin, ModelSerializer):
    include_arg_name = 'currency'
    pass


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )


class BalanceSerializer(MyModelSerializer):

    class Meta:
        model = Balance
        fields = '__all__'


class RefillSerializer(MyModelSerializer):

    def validate(self, data):
        if data['sum'] <= 0:
            raise validators.ValidationError('Сумма должна быть больше 0')
        return(data)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('sender', 'receiver', 'operation', )


class WithdrawSerializer(MyModelSerializer):

    def validate(self, data):
        if data['sum'] <= 0:
            raise validators.ValidationError('Сумма должна быть больше 0')
        return(data)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('sender', 'receiver', 'operation',)


class TransferSerializer(MyModelSerializer):

    def validate(self, data):
        if data['sum'] <= 0:
            raise validators.ValidationError('Сумма должна быть больше 0')
        return(data)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('sender', 'receiver', 'operation', )
