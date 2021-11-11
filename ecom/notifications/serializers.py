from rest_framework import serializers
from .models import *


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications

        fields = '__all__'
