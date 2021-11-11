from rest_framework import serializers
from .models import *


class PaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model =PaymentMethods

        fields = '__all__'
        
