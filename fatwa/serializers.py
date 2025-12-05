from rest_framework import serializers
from .models import Category, Fatwa

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class FatwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatwa
        fields = ['id', 'name', 'address', 'category', 'question', 'answer', 'reference', 'created_at', 'updated_at']