# userapp/urls.py
from django.urls import path
from .views import user_create_view
from . import views


urlpatterns = [
    path('create/', user_create_view, name='user-create'),
    path('', views.user_list_view, name='list_users'),
]
