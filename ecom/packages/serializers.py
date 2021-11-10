from rest_framework import serializers
from .models import *


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages

        fields = '__all__'
        

class PackagesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesType

        fields = '__all__'


class PackagesTypeAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesTypeAttributes

        fields = '__all__'