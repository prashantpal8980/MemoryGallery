from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.memorygallery, name='memorygallery'),
    path('gallery/', views.gallery, name='gallery'),
   
] 