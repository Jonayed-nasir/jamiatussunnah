from django.urls import path, include
from .views import NoticePostView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

urlpatterns = [

    path('api/', NoticePostView.as_view(), name='notice-posts')

]
