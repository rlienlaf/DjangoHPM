from django.urls import path
from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.post_list, name='post_list'),
    path('post/<int:question_id>', views.detail, name='detail'),
]
