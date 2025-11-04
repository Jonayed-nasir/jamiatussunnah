from rest_framework import serializers
from .models import NoticePost



class NoticePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = ['title', 'content', 'iamge', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']