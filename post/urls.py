from django.urls import path, include
from .views import NoticePostView, BefaqResultDetailsView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

urlpatterns = [

       path('api/<int:pk>/', NoticePostView.as_view(), name='notice-detail'),
    path('api/befaq_result', BefaqResultDetailsView.as_view(), name='befaq_result')

]
