"""Defines URL patterns for users"""

from django.urls import path, include
from . import views


app_name = 'users'  # This is required when using a namespace
urlpatterns = [
    # Include default Django auth URLs
    path('', include('django.contrib.auth.urls')),
    # Regisration page.
    path('register/', views.register, name='register')
]
