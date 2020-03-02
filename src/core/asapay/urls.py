"""App urls"""
from django.urls import path
from .views import dashboard

app_name = 'asapay'

urlpatterns = [
    path('', dashboard, name='dashboard')
]