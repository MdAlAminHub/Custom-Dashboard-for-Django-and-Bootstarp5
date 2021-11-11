from rest_framework import serializers
from .models import *


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers

        fields = '__all__'
