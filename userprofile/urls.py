from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/',views.profile,name='profile'),
    path('post/<int:post_id>/',views.post_detail,name='post_detail'),
    path('edit/', views.edit, name='edit') 
]

