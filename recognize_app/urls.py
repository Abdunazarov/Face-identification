from django.urls import path
from .views import faceID


urlpatterns = [
    path('faceID/', faceID),
]