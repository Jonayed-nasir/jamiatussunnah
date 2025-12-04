from django.shortcuts import render
from .serializer import NoticePostSerializer, BefaqResultDetailsSerializer
from .models import NoticePost, BefaqResultDetails
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

class NoticeDetailView(APIView):
    def get(self, request, pk):
        try:
            notice = NoticePost.objects.get(pk=pk)
        except NoticePost.DoesNotExist:
            return Response({'error': 'Notice not found'}, status=404)

        serializer = NoticePostSerializer(notice)
        return Response(serializer.data)

class BefaqResultDetailsView(APIView):
    def get(self, req):
        queryset = BefaqResultDetails.objects.all()
        serializer = BefaqResultDetailsSerializer(queryset, many=True)

        return Response(serializer.data)



