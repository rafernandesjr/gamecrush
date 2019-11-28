from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<int:room_name>/', views.room, name='room'),
]
