
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:pk>', views.detail_post, name='detail-post'),
    path('create_post/', views.create_post, name='create-post'),
    path('posts/update/<int:pk>', views.update_post, name='update-post'),
    path('posts/delete/<int:pk>', views.delete_post, name='delete-post'),
]
