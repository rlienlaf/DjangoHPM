from django.urls import path
from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]
