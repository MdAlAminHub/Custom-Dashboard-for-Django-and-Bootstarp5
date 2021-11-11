from rest_framework import serializers
from .models import *


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries

        fields = '__all__'
        

class TaxClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxClasses

        fields = '__all__'
        
        
class TaxRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaxRates

        fields = '__all__'


class ZonesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zones

        fields = '__all__'
