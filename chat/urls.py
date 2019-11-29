from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<int:room_name>/<int:user_id>/', views.room, name='room'),
]
