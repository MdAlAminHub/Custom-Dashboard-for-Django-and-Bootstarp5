from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = '__all__'
        

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories

        fields = '__all__'
