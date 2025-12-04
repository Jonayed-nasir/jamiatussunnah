from django.urls import path
from .views import admission_api
urlpatterns = [
    path('apply/', admission_api, name='admission_api'),
]