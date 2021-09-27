from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ConvertCoin

routers = DefaultRouter()

urlpatterns = [
    path("converter", ConvertCoin.as_view()),
    path("", ConvertCoin.as_view()),
]
