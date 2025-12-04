from django.shortcuts import render
from .serializer import NoticePostSerializer, BefaqResultDetailsSerializer
from .models import NoticePost, BefaqResultDetails
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.

class NoticePostView(APIView):
    def get(self, request):
        queryset = NoticePost.objects.all().order_by('-updated_at', '-created_at')
        posts = queryset[:5]  # latest 5 notices
        serializer = NoticePostSerializer(posts, many=True)
        return Response(serializer.data)

class NoticeDetailView(APIView):
    def get(self, request, pk):
        notice = get_object_or_404(NoticePost, pk=pk)
        serializer = NoticePostSerializer(notice)
        return Response(serializer.data)

class BefaqResultDetailsView(APIView):
    def get(self, req):
        queryset = BefaqResultDetails.objects.all()
        serializer = BefaqResultDetailsSerializer(queryset, many=True)

        return Response(serializer.data)



