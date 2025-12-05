from django.shortcuts import render
from .models import Message, GuestUser
from .serializers import GuestUserSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class MessageView(APIView):
    def get(self, request):
        guest_id = request.GET.get('guest_id')
        if guest_id:
            queryset = Message.objects.filter(sender_id=guest_id) | Message.objects.filter(sender=None)
        else:
            queryset = Message.objects.all().order_by('-created_at')
        queryset = queryset.order_by('-created_at')
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
    def post(self, request):
        name = request.data.get('name', '').strip()
        email = request.data.get('email', '').strip()

        if not name:
            return Response({'error': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        guest_user, created = GuestUser.objects.get_or_create(email=email, defaults={'name': name})
        if not created:
            guest_user.name = name
            guest_user.save()
        serializer = GuestUserSerializer(guest_user)
        return Response(serializer.data, status=status.HTTP_200_OK)