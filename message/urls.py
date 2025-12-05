from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageView.as_view(), name='message-list'),
    path('guest-user/', views.GuestUserView.as_view(), name='guest-user'),
]
