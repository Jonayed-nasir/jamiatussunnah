from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('fatwas/', views.FatwaListView.as_view(), name='fatwa-list'),
    path('fatwas/<int:pk>/', views.FatwaDetailView.as_view(), name='fatwa-detail'),
]
