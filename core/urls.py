from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
