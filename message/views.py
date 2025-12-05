from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class MessageView(APIView):
    def get(self, request):
        queryset = Message.objects.all().order_by('-created_at')
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)