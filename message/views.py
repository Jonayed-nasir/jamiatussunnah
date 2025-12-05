from django.shortcuts import render
from .models import Message, GuestUser
from .serializers import GuestUserSerializer, MessageSerializer
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
    
class GuestUserView(APIView):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        ip_address = self.get_client_ip(request)
        name = request.data.get('name', "").strip()
        if not name:
            return Response({"error": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)
        user, created = GuestUser.objects.get_or_create(ip_address=ip_address, defaults={'name': name})
        if not created:
            user.name = name
            user.save()
        serializer = GuestUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)