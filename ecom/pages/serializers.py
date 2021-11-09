from rest_framework import serializers
from .models import *


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages

        fields = '__all__'
