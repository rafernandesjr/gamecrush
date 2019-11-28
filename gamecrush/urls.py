from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from .settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

from . import views

from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:auth_id>/', views.index, name='index'),

    path('<int:auth_id>/registro/', views.upload, name='registro'),
    path('<int:auth_id>/acesso/', views.signin, name='acesso'),
    path('<int:auth_id>/perfil/<str:user_id>/', views.profile, name='perfil'),
    
    path('<int:auth_id>/chat/', include('chat.urls'), name='chat'),
    
    path('<int:auth_id>/update/<int:user_id>', views.update_user, name='update'),
    path('<int:auth_id>/delete/<int:user_id>', views.delete_user),
    path('admin/', admin.site.urls, name='admin')
    
]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
