from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home1/', views.home1, name='home1'),
    path('members_preview/', views.members_preview, name='members_preview'),
    path('register/', views.register, name='register'),
    path('<str:member_id>/', views.view_details, name='view_details'),
]
