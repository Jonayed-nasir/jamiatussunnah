from rest_framework import serializers
from .models import NoticePost



class NoticePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = ['title', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']