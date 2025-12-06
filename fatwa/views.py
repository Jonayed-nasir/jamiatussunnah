from django.shortcuts import render
from .models import Category, Fatwa
from .serializers import CategorySerializer, FatwaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.


class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.all().order_by('name')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
class FatwaListView(APIView):
    def get(self, request):
        queryset = Fatwa.objects.all().order_by('-updated_at', '-created_at')
        serializer = FatwaSerializer(queryset, many=True)
        return Response(serializer.data)

class FatwaDetailView(APIView):
    def get(self, request, pk):
        fatwa = get_object_or_404(Fatwa, pk=pk)
        serializer = FatwaSerializer(fatwa)
        return Response(serializer.data)

