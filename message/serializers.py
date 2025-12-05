from rest_framework import serializers
from .models import Message, GuestUser

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.name', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_name', 'body', 'created_at']

class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUser
        fields = ['id', 'name', 'ip_address', 'created_at']