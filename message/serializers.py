from rest_framework import serializers
from .models import Message, GuestUser

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'body', 'created_at']

class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUser
        fields = ['id', 'name', 'ip_address', 'created_at']