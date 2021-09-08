from rest_framework.serializers import ModelSerializer

from .models import User, Payment


#class MyModelSerializer(QueryFieldsMixin, ModelSerializer):
    #include_arg_name = 'show'
    #exclude_arg_name = 'exclude'
    #pass


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
