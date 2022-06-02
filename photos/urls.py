from django.urls import path 
from . import views
# from .views import HomeView, PictureView


# app_name = 'photos'

urlpatterns = [
    path('', views.gallery, name='gallery',),
    path('photo/<str:pk>/', views.viewPhoto, name='photo',),
    path('search/', views.search, name='search'),   
     # path('data-json/', PictureView.as_view(), name='data-json'),
]

