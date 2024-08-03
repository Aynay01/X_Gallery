from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_gallery, name='photo_gallery'),  # Route root URL to the photo_gallery view
]