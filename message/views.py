from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class MessageView(APIView):
    def get(self, request):
        queryset = Message.objects.all().order_by('-created_at')
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
    
   
    def post(self, request):
        # print(request.body)  # debug: ki asche body te
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)  # debug: ki save holo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    