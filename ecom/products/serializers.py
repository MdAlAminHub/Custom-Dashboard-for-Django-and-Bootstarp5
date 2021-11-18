from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = '__all__'
        

class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes

        fields = '__all__'
