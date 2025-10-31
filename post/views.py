from django.shortcuts import render
from .serializer import NoticePostSerializer
from .models import NoticePost
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.


class NoticePostView(APIView):
    def get(self, request):
        queryset = NoticePost.objects.all().order_by('-created_at', 'updated_at')
        posts = queryset[:5]
        serializer = NoticePostSerializer(posts, many=True)

        return Response(serializer.data)



