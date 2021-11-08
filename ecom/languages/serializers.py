from rest_framework import serializers
from .models import *


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages

        fields = '__all__'
