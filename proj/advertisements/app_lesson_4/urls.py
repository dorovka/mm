from django.urls import path
from .views import index, dz

urlpatterns = [
    path('', index),
    path('lesson_4/', dz)
]