from django.urls import path, include
from .views import NoticePostView, BefaqResultDetailsView, NoticeDetailView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

urlpatterns = [

       path('api/<int:pk>/', views.NoticeDetailView.as_view(), name='notice-detail'),
       path('api/', views.NoticePostView.as_view(), name='notice-list'),
       path('api/all/', views.GetAllNoticePostsView.as_view(), name='notice-list-all'),
    path('api/befaq_result', views.BefaqResultDetailsView.as_view(), name='befaq_result')

]
