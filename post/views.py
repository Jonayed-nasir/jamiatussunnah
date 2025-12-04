from django.shortcuts import render
from .serializer import NoticePostSerializer, BefaqResultDetailsSerializer
from .models import NoticePost, BefaqResultDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.


class NoticePostView(APIView):
     def get(self, request, pk):
        try:
            pk = int(pk)
        except ValueError:
            return Response({"error": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            notice = NoticePost.objects.get(pk=pk)  # single object
        except NoticePost.DoesNotExist:
            return Response({"error": "Notice not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoticePostSerializer(notice)  # many=True নয়, single object
        return Response(serializer.data)
class BefaqResultDetailsView(APIView):
    def get(self, req):
        queryset = BefaqResultDetails.objects.all()
        serializer = BefaqResultDetailsSerializer(queryset, many=True)

        return Response(serializer.data)



